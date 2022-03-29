# CHALLENGE 19 - CODE RED CHAOS

# Note: no preprocessing 
#       -> CRC(0) = 0 
#       -> CRC(msg \oplus interf) = CRC(msg) \oplus CRC(interf)
# Goal:
#       CRC(msg \plus interf) = CRC(msg)
#       -> CRC(interf) = 0 for all interfs
# How?
#       We make use of gcd algorithm
#       Use crc operation instead of regular mod
#       Larger value as divisor, smaller as polynomial


# Bitwise XOR
def xor(a, b):
    
    # initialize result
    result = []
    
    # transverse all bits
    # if bits are same, XOR is 0, else 1
    for a, b in zip(a,b):
        result.append('0' if a==b else '1')
    
    return ''.join(result)

# Calculate CRC with a custom polynomial
# The polynomial should be smaller than the number
def crc(value, poly):
   
    # number of bits to be XORed at a time
    n = len(poly)
    
    # original number of bits of value
    m = len(value)
    
    # append trailing zeros for remainder
    value += "0"*(n-1)
    
    tmp = value[0:n]    
    for i in range(m):
        if tmp[0] == '1':
            # if leading 0 just go to next iteration (quotient is 0)
            tmp = xor(tmp, poly)
        # remove leading number
        tmp = tmp[1:]
        if i < m-1:
            # while not last iteration, put down next number
            tmp += value[n+i]

    return tmp


# Find gcd (with crc instead of regular mod)
def gcd_crc(a, b):
    
    # Find gcd
    # Note that crc works with binary repr. as string
    while b != 0:
        t = b
        r = crc(f"{a:b}",f"{b:b}")
        b = int(r,2)
        a = t
        
    
    # Remove trailing 0s
    # a != 0, but just in case
    if a > 0:
        while (a & 1) == 0:
            a >>= 1
    
    return a





# A IMPLEMENTAR:
# ESCRIURE SORTIDA EN HEXA


# Print polynomial given number of case and integer
def printPoly(c, n):
    nstr = hex(n)[2:]
    print(f"Case #{c}: {nstr}")


N = int(input())

for n in range(N):


    I = int(input()) # number of interferences
    interfs = []
    for _ in range(I):
        interf = input() # interference in hex
        interf = int(interf, 16) # convert to integer
        interfs.append(interf)
        
    # if there's only 1 interf, just remove trailing zeros
    if I == 1:
        first = interfs[0]
        while (first & 1) == 0:
            first >>= 1
        printPoly(n+1, first)
        continue
        
    # start with smaller numbers to reduce cost for crc
    # smaller number used as polynomial
    interfs = sorted(interfs)
    poly = interfs[0]
    for next in interfs:
        if poly == 1:
            # if poly is 1, then gcd is for sure 1
            # avoid calling crc since it will return an empty string
            break
        poly = gcd_crc(next, poly)
        
    # print result
    printPoly(n+1, poly)
    
    
    
   
