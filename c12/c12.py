# CHALLENGE 12 - THE CRYPTO BUBBLE

from collections import deque


# BFS to calculate all shortest paths
# Get parent of each node in shortest path
def bfs(transactions, parent, start = "BTC"):

    dist = {x: float("inf") for x in transactions}

    q = deque()

    # First iteration (start current node)    
    # Note that dist[start] is still inf
    for next in transactions[start]:
        dist[next] = 1
        q.append(next)
        parent[next].clear()
        parent[next].append(start)
    
    while q:
        
        node = q.popleft()
        
        for next in transactions[node]:
            
            if (dist[next] > dist[node] + 1):
                # Shorter distance is found
                dist[next] = dist[node] + 1
                q.append(next)
                parent[next].clear()
                parent[next].append(node)
                
            elif (dist[next] == dist[node] + 1):
                # Another candidate parent for shorter path found
                parent[next].append(node)
                

# Find maximum rate of a shortest path
# Start from node and make its way up until "BTC"
# First is True only in the first call with node="BTC"
def find_path(transaction, parent, node ="BTC", first=False):
    
    # Initial node
    if node == "BTC" and not first:
        return 1
    
    # Get max rate between all parents, including transaction from parent to node
    max_rate = 1
    for par in parent[node]:
        rate = find_path(transaction, parent, par)
        rate *= transaction[par][node]
        if rate > max_rate:
            max_rate = rate
    
    # Return max rate
    return max_rate

# MAIN
    
N = int(input())

for n in range(N):

    # Transactions dictionary
    transactions = {}

    # Read input and fill dict
    M = int(input())
    for _ in range(M):
        
        _, K = input().split()
        for _ in range(int(K)):
            
            orig, rate, dest = input().split("-")
            rate = int(rate)
            
            # We don't want to lose all the money
            #if rate == 0:
            #    continue
            
            # Make sure all possible keys are present
            if orig not in transactions:
                transactions[orig] = {}
            if dest not in transactions:
                transactions[dest] = {}
                
            # Add transaction
            if dest not in transactions[orig]:
                # add rate of transaction
                transactions[orig][dest] = rate
            elif rate > transactions[orig][dest]:
                # update rate of transaction if better than previous
                transactions[orig][dest] = rate
                
    # Check that somewhere to start and run algorithm
    if "BTC" not in transactions:
        rate = 1
    else:
        parent = {x: [] for x in transactions}
        bfs(transactions, parent)
        rate = find_path(transactions, parent, first=True)
        
    print(f"Case #{n+1}: {rate}")
