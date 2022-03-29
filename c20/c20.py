# CHALLENGE 20 - HIDDEN TOY STORY

from PIL import Image, ImageDraw

# HELPER FUNCTIONS

# integer distance in rhb pixel
def rgb_distance(pxl1, pxl2):
    dr = abs(pxl1[0] - pxl2[0])
    dg = abs(pxl1[1] - pxl2[1])
    db = abs(pxl1[2] - pxl2[2])
    return dr + dg + db
    
# check if next pixel follows black line
def check_pixel(pixels, pos, next, visited):
    # don't go back (we only need to check last two positions)
    if next in visited:
        return False
    pxl1 = pixels.getpixel(pos)
    pxl2 = pixels.getpixel(next)
    return rgb_distance(pxl1, pxl2) < 30

        
# check surrounding pixels
# first check surrounding four
# if no match, check diagonals
# Note: in the first pad this can fail in the peak of the N. There, prioritize going up.
def next_pixel(pixels, pos, visited):
    global filename
    
    x, y = pos
    directions = [
        (x,y-1),
        (x+1,y),
        (x-1,y),
        (x,y+1),
        (x+1,y+1),
        (x+1,y-1),
        (x-1,y+1),
        (x-1,y-1)
    ]
    
    # 1st and 2nd tablets
    if filename != "fight_run.png":
        for d in directions:
            if check_pixel(pixels, pos, d, visited):
                return d
        # End of line reached
        return None
        
    # 3rd tablet: crossings allowed
    valid = []
    for d in directions:
        if check_pixel(pixels, pos, d, visited):
            valid.append(d)
    # normal cases: 
    # 1 - only one way to go
    # 2 - turn: prioritize going straigh over diagonal
    n = len(valid)
    if n == 1 or n == 2:
        return valid[0]
    # too many places to go: unvisited path crossing, just go straight
    xlast, ylast = visited[-2]
    dx = x - xlast
    dy = y - ylast
    next = (x + dx, y + dy)
    if n > 2:
        return next
        
    # no way to go
    # check if we can go straight (jump into visited bridge)
    if check_pixel(pixels, pos, (x+2*dx, y+2*dy), visited):
        return next
    # check if we can go straigh (jump from visited bridge)
    if check_pixel(pixels, visited[-2], next, visited):
        return next
    return None
    
def print_surroundings(pixels, pos):
    x, y = pos
    directions = [
        (x+1,y),
        (x-1,y),
        (x,y+1),
        (x,y-1),
        (x+1,y+1),
        (x+1,y-1),
        (x-1,y+1),
        (x-1,y-1)
    ]
    print(pos, " - ", pixels.getpixel(pos))
    for d in directions:
        print(d, " - ", pixels.getpixel(d))
    
    
# MAIN
    
# CHOOSE TABLET
#filename = "hidden_toy_story.png"
#filename = "now_in_color.png"
filename = "fight_run.png"

# open image
img = Image.open(filename)

# get image dimensions
# width = 500
# height = 405
width, height = img.size

# get colors
# we could just use RGB, but can't bother changing the code
pixels = img.convert("RGBA")

# Look for starting position (by hand)
# Code was removed but the idea was the following
#   - Choose x0, y0
#   - Iterate through all the positions between x0 and xf = x0 + dx
#   - Add a marker at x0 and at xf
#   - If border from red to grey was between the markers, find position of first grey pixel
#   - Do the same for y, going up until finding black line
# The starting position of the line is the same for all tablets
# (x0,y0) = (81,114)

x0 = 81
y0 = 114

# Follow line starting from (x0,y0) until its end

pos = (x0,y0)
visited = [pos]
data = [pos]
g = 0
while True:
    # draw pixel
    img.putpixel(pos, (0,g,0,0))
    g = (g+1)% 256
    #print(pos, " - ", pixels.getpixel(pos))
    
    # next position
    pos = next_pixel(pixels, pos, visited)
    
    # end of line
    if not pos:
        break
    
    visited.append(pos)
    
    # for tablet 1 and 2
    # data.append(pos)
    
    # for tablet 3
    # Tried:
    #   - using all pixels (possibly repeated)
    #   - first visited only
    #   - according to color of line
    # Best result: first
    
    if pos not in data:
        data.append(pos)
    continue

    
    # for tablet 3
    pxl1 = pixels.getpixel(pos)
    pxl2 = pixels.getpixel(visited[-2])
    if rgb_distance(pxl1, pxl2) < 100:
        data.append(pos)
    
# prints for debugging/analysis
    
#print_surroundings(pixels, visited[-2])
#print(visited[-10:])
print("Num pixels in line: ", len(visited))

# show or store image (with line colored in green, to check path)

#img.show()
img.save("mod3.png")


# Get information in the channels
# Data found to be in the LSB of rgb
aux = []

# Remove duplicates
for pxl in data:
    #print(pxl)
    #print(pxl, " - ", pixels.getpixel(pxl))
    r, g, b, a = pixels.getpixel(pxl)
    r = r & 1
    g = g & 1
    b = b & 1
    aux.append(r)
    aux.append(g)
    aux.append(b)

for x in aux:
    print(x, end="")
print()
