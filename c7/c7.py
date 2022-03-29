# CHALLENGE 7 - ESCAPE OR DIE

import socket
from collections import deque

# Check if movement is valid (needed in order to move there later)
def checkNextCoord(direct):
    
    s.send(direct.encode())
    data = s.recv(1024).decode()
    if data.split()[0] == "Ouch.":
        return False
    
    # Go back
    reverse = {
        "west": "east",
        "east": "west",
        "north": "south",
        "south": "north"
    }
    s.send(reverse[direct].encode())
    data = s.recv(1024).decode()
    return True

# Get next coordinates based on current coordinates and direction
def getNextCoord(coord, direct):
    
    step = {
        "west": (1,0),
        "east": (-1,0),
        "south": (0,-1),
        "north": (0,1)
    }
    
    x0, y0 = coord
    dx, dy = step[direct]
    return (x0+dx, y0+dy)
    

# Connect to daemon
host = "codechallenge-daemons.0x14.net"
port = 4321
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

# Search data
# - visited: set of visited locations, including shortest path to them 
#            Last element should be the key location itself
# - q: queue of visited locations yet to explore
# - pos: current position
q = deque()
pos = (0,0)
q.append(pos)
visited = {
    pos: [pos]
}

# Initial read
data = s.recv(1024).decode()
print(data)

while True:

    # Go to next position in the queue
    pos = q.popleft()
    s.send(f"go to {pos[0]},{pos[1]}".encode())
    data = s.recv(1024).decode()
    print(data)
    
    # Check if we are at exit
    s.send("is exit?".encode())
    data = s.recv(1024).decode()
    print(data)
    if data.split()[0] != "No.":
        print(visited[pos])
        break
    
    # Check where we are
    #s.send("where am I".encode())
    #data = s.recv(1024).decode()
    #coord = eval(data)
    #print(coord)
    
    # Get possible directions
    s.send("look".encode())
    data = s.recv(1024).decode()
    directions = data.split()[10:]
    print(directions)
    
    for d in directions:
        
        # If movement invalid, don't take into account
        if not checkNextCoord(d):
            continue
            
        # If valid, append coordinates to queue to visit later
        next = getNextCoord(pos, d)
        if next not in visited:
            q.append(next)
            visited[next] = visited[pos] + [next]
