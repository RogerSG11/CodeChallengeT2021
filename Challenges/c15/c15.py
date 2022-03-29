# CHALLENGE 15 - THE REVENGE OF THE NON-TUENTISTIC NUMBERS

import sys


# Check if number is tuentistic
# Assumin n < 1e8 + 7
def isTuentistic(n):
    if n // 10 % 10 == 2:
        return True
    if n // int(1e4) % 10 == 2:
        return True
    if n // int(1e7) % 10 == 2:
        return True
    return False
    

# Return n!/(prod of all non-tuentistic nums) mod p
# Naive approach, linear cost
# start, fstart provide intermediate result
# fstart = naiveNonTuentiFact(start)
def naiveNonTuentiFact(n, start=1, fstart=1):
    global p
    
    res = fstart
    for x in range(start+1,n+1):
        if not isTuentistic(x):
            res = (res * x) % p
    return res

# Get multiplication of non-tuentistic nums up to N
# Result mod p
# p = 1e8 + 7
def nontuentisticmult(n):
    global p
    global facts

    # if n >= m then n! = 0 (mod m) because m is factor of n
    if n >= p:
        return 0
        
    key = n // 100
    fkey = facts[key]
    res = naiveNonTuentiFact(n, key*100, fkey)
    
    return res




# PRECALCULATIONS AND GLOBALS

# Global: modulus
p = int(1e8) + 7

# Precalculate factorials
# facts[n//100] = factorial_mod(n*100)
facts = []
x = 1
facts.append(x)
for key in range(1, int(1e6)):
    fkey = naiveNonTuentiFact(key*100, (key-1)*100, facts[key-1])   
    facts.append(fkey)
    # Checkpoints during execution
    if key % int(1e5) == 0:
        print(f"Precalc {key}", file=sys.stderr)
     

# MAIN

print("Input num of cases", file=sys.stderr)

# get inputs and do calculation

C = int(input())

for c in range(C):

    print(f"Case {c+1}", file=sys.stderr)
    
    N = int(input())
    
    res = nontuentisticmult(N)
    print(f"Case #{c+1}: {res}")
    
print(f"Finished", file=sys.stderr)
