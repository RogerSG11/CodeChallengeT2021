# CHALLENGE 16 - WHERE ARE THE PRIMES AT?

import socket
import math
import numpy as np
import collections
import random

# socket connection

host = "codechallenge-daemons.0x14.net"
port = 7162
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

# least common multiple
def lcm(a,b):
    return abs(a*b) // math.gcd(a,b)
    
# helper for communication: send data string, receive data string
def comm(data):
    s.send(data.encode())
    ret = s.recv(1024).decode()
    return ret


# find prime factors
def prime_factors(n):
    i = 2
    factors = set()
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.add(i)
    if n > 1:
        factors.add(n)
    return factors
    
# check if prime
def isPrime(n):
    if n<=3: return True
    if n%2==0 or n<2: return False
    for i in range(3, int(n**0.5)+1, 2):   # only odd numbers
        if n%i==0:
            return False    

    return True


# First data received: N and Q
data = s.recv(1024).decode().split()
N = int(data[0])
Q = int(data[1])


# save info
factors = [1] * N
primes = [True] * N
pivots = {}
new_pivots = []

#primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

# first sweep
for i in range(0,N-1):
    
    x = comm(f"? {i+1} {i+2}")
    x = int(x)
    
    factors[i] = lcm(factors[i], x)
    factors[i+1] = lcm(factors[i+1], x)
    
# mark non primes and choose pivots
for i in range(0,N):
    
    x = factors[i]
    
    if not isPrime(x):
        primes[i] = False
    
    for prime in prime_factors(x):
        if prime not in pivots:
            pivots[prime] = x
            new_pivots.append(x)
    
while new_pivots and collections.Counter(primes)[True] > 26:
    
    pivot = new_pivots.pop(0)
    
    for i in range(0, N):
        
        if i == pivot: 
            # don't repeat
            continue
        
        if primes[i] == False:
            # we already know it's not a prime
            continue
        
        x = int(comm(f"? {pivot+1} {i+1}"))
        
        # check if we got a new pivot
        for prime in prime_factors(x):
            if prime not in pivots:
                pivots[prime] = x
                new_pivots.append(x)
                
        # update factors
        factors[pivot] = lcm(factors[pivot], x)
        if primes[pivot] and not isPrime(factors[pivot]):
            primes[pivot] = False
        
        factors[i] = lcm(factors[i], x)
        if not isPrime(x):
            primes[i] = False
            
count = collections.Counter(primes)[True]
print("Pivot method: ", count)
            
if count > 26:
    # we have eliminated most candidates
    # pass another filter
    for i in range(0, N):
        if not primes[i]:
            continue
        for j in range(i+1, N):
            if not primes[j]:
                continue
            x = int(comm(f"? {i+1} {j+1}"))
            
            factors[j] = lcm(factors[j], x)
            if not isPrime(factors[j]):
                primes[j] = False
            
            factors[i] = lcm(factors[i], x)
            if not isPrime(factors[i]):
                primes[i] = False
                break 
            
count = collections.Counter(primes)[True]
print("Bruteforce method: ", count)

if count > 26:
    # Usually we are missing 9, 25, 49
    # Counter is then 27 or 28 or 29
    # Cannot distinguish them from 3/5/7 and they have few multiples
    anomalies = []
    nums = {1, 3, 5, 7}

    for i in range(N):
        fi = factors[i]
        if fi not in nums:
            continue
        for j in range(i+1, N):
            fj = factors[j]
            if fj not in nums:
                continue
            x = int(comm(f"? {i+1} {j+1}"))
            if x>1:
                anomalies.append((i,j))
                
    # From anomalies, choose at random
    for x, y in anomalies:
        b = bool(random.getrandbits(1))
        if b:
            primes[x] = False
        else:
            primes[y] = False
        
count = collections.Counter(primes)[True]
print("Anomaly method: ", count)
        
# send result to judge
positions = []
for i in range(N):
    if primes[i]:
        positions.append(str(i+1))
query = "! " + " ".join(positions)
data = comm(query)
print(data)
