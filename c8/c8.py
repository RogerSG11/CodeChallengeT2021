# CHALLENGE 8 - AWESOME SALES INC!

# https://www.geeksforgeeks.org/articulation-points-or-cut-vertices-in-a-graph/

# Search critical nodes via Tarjan's alg.
# node -> node to be visited next
# edges -> edges of graph
# visited -> whether each node has been visited
# disc -> discovery times for each node 
# parent -> parent node in DFS tree
# low -> min(disc(u), disc(w)) for u,w satisfying some conditions
# crits -> critical nodes (articulation points)
# time -> array with a single int, time at which node is visited
def critsDFS(node, edges, visited, crits, parent, disc, low, time):

    # count children in current node
    children = 0
    
    # mark current node as visited
    visited[node] = True
    
    # Init discovery time and low value
    disc[node] = time[0]
    low[node] = time[0]
    time[0] += 1
    
    # Recur for all vertices adjacent to this vertex
    for nxt in edges[node]:
        
        # If next is not visited yet, then make it a child of node
        # in DFS tree and recur for it
        if not visited[nxt]:
        
            parent[nxt] = node
            children += 1
            critsDFS(nxt, edges, visited, crits, parent, disc, low, time)
            
            # Check if the subtree rooted with next has a connection to
            # one of the ancestors of node
            low[node] = min(low[node], low[nxt])
            
            # node is an articulation point in the following cases
            # (1) node is roont of DFS tree and has two or more children
            if parent[node] == "" and children > 1:
                crits.add(node)
            
            # (2) If node is not root and low value of one of its children is more
            # than discovery value of u
            if parent[node] != "" and low[nxt] >= disc[node]:
                crits.add(node)
        
        # Update low value of node for parent function calls        
        elif nxt != parent[node]:
            low[node] = min(low[node], disc[nxt])
            
# MAIN

C = int(input())

for c in range(C):

    edges = {}
    visited = {}
    disc = {}
    low = {}
    parent = {}
    
    T = int(input())
    for t in range(T):
        origin, dest = input().split(",")
        
        if origin not in edges:
            edges[origin] = []
            visited[origin] = False
            disc[origin] = float("Inf")
            low[origin] = float("Inf")
            parent[origin] = ""     
            
        if dest not in edges:
            edges[dest] = []
            visited[dest] = False
            disc[dest] = float("Inf")
            low[dest] = float("Inf")
            parent[dest] = ""     
        
        edges[origin].append(dest)
        edges[dest].append(origin)
        
    crits = set() # use set to avoid duplicates
    time = [0] # workaround to have mutable int
    
    for node in edges.keys():
        if not visited[node]:
            critsDFS(node, edges, visited, crits, parent, disc, low, time)
            
    if not crits: # set is empty
        print(f"Case #{c+1}: -")
    else:
        print(f"Case #{c+1}: {','.join(sorted(crits))}")
