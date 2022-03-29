# CHALLENGE 11 - ALOT ANOTHER LIBRARY OF TOOLS

import numpy as np
from collections import Counter

#from os.path import commonprefix
# prefix = commonprefix([list of strings])
# O(n) in time

T = int(input())

for t in range(T):

    
    N, K = map(int, input().split())

    maxlen = 0 # length of largest function
    functions = []
    
    for _ in range(N):
        f = input()
        functions.append(f)
        if len(f) > maxlen:
            maxlen = len(f)
       
    # Sort functions
    # Functions sharing prefix end up together
    # functions = sorted(functions)
    
    # Build table with all prefixes, padded to maximum length
    # 2D numpy array for easier treatment
    table = []
    for f in functions:
        row = [f[:j] for j in range(1, len(f)+1)] + [""]*(maxlen - len(f))
        table.append(row)
    table = np.array(table)
    
    # Mask to remove used elements
    mask = np.ones(len(functions), dtype=bool)
    
    # Total score
    score = 0
    
    # Iterate through columns
    for column in table.T[::-1]:
    
        # Apply mask to column and keep only non-zero elements
        col = column[mask]
        col = col[np.nonzero(col)]
        
        # If no elements available, skip to next iteration
        if len(col) == 0:
            continue
            
        # Check all elements with frequence >= K
        for func, count in Counter(col).most_common():
        
            if count < K:
                break
        
            # Distribute as many as possible in whole files
            files = count // K
            
            # Increment score
            score += files*len(func)
            
            # Update mask with used elements
            if files > 0:
                idxs = np.where((column == func) & (mask))[0][:files*K]
                mask[idxs] = False
        
    # Print result
    print(f"Case #{t+1}: {score}")
