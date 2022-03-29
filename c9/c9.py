# CHALLENGE 9 - COLLISIONS

import numpy as np

# x, y = position of both sprites (in x or y coordinate)
# a, b = dimensions of both sprites (height or width)
# Result (coordinate, dimension)
# Note: if dim negative or zero, there's no overlap
def findOverlap(x, y, a, b):

    l = max(x,y)
    r = min(x+a, y+b)
    
    dim = r - l
    return (l, dim)
    
    

# pos1 = position of first sprite = (identifier, x, y)
# pos2 = position of second sprite
# sprites = full list of sprites (as 2D numpy arrays)
# Return:
#   -1 = no overlap in x
#    0 = no overlap in y or overlap w/o collision
#    1 = collision
def findCollision(pos1, pos2, sprites):
    i1, x1, y1 = pos1
    i2, x2, y2 = pos2
    
    s1 = sprites[i1]
    s2 = sprites[i2]
    
    h1, w1 = s1.shape
    h2, w2 = s2.shape
    
    # Collision in X
    x, w = findOverlap(x1, x2, w1, w2)
    
    # Collision in Y
    y, h = findOverlap(y1, y2, h1, h2)
    
    # No overlap
    if w <= 0:
        return -1
    elif h <= 0:
        return 0
        
    # Get overlapping region of each sprite
    area1 = s1[y-y1:y-y1+h, x-x1:x-x1+w]
    area2 = s2[y-y2:y-y2+h, x-x2:x-x2+w]
    
    # overlap both areas
    overlap = area1 & area2
    
    # If overlap has non-zero element there's a collision
    return int(np.any(overlap))


# MAIN

T = int(input())

# Read and store sprites
    
sprites = [] # sprites[num_sprite][row_sprite][col_sprite]

D = int(input())
for _ in range(D):

    sprite = []
    
    _, H = map(int, input().split())
    for _ in range(H):
        row = [int(x) for x in input()]
        sprite.append(row)
        
        
    sprite = np.array(sprite)
    sprites.append(sprite)
    
# Perform cases
    
for t in range(T):

    P = int(input())
    
    positions = []
    for _ in range(P):
        I, X, Y = map(int, input().split())
        positions.append((I,X,Y))
        
    # Sort by x
    positions = sorted(positions, key = lambda x : x[1])
    
    collisions = 0
        
    for i in range(len(positions)):
        # Compare next sprites only until no overlap possible in x
        for j in range (i+1, len(positions)):
            res = findCollision(positions[i], positions[j], sprites)
            if res < 0:
                break
            collisions += res

    print(f"Case #{t+1}: {collisions}")
