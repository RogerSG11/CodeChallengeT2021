# CHALLENGE 20 - HIDDEN TOY STORY
# AUXILIARY CODE: DECODE MESSAGE FROM LAST IMAGE


# AUXILIARY FUNCTIONS

# Read n bytes
# Use global file decriptor f
# Update global bytes_read
def read(n):
    global f
    global bytes_read
    bytes_read += n
    return f.read(n)

# Separate good ascii vs bad/non ascii
def is_good_ascii(x):
    return x.is_ascii() and (x.is_printable() or x == "\n")
    
# hexstring to signed int
# https://stackoverflow.com/questions/6727875/hex-string-to-signed-int-in-python-3-2
def hex2int(hexstr, bits):
    value = int(hexstr, 16)
    if value & (1 << (bits-1)):
        value -= 1 << bits
    return value


# MAIN

filename = "output3.dat"
f = open(filename, "rb")

fout = open("output3.txt", "wb")

f.read(15) # remove first 15 bytes
n = int(f.read(3).decode('ascii')) # size of message in bytes
f.read(2) # remove 2 newlines



bytes_read = 0
window = [] # sliding window

woff = 20 # window position offset

while bytes_read < n:
    
    # 1st byte is always non-ascii
    # it gives the position of the non-ascii characters in the block
    # binary repr. must be interpreted in reverse
    byte = read(1).hex()
    block = f"{int(byte,16):0>8b}"[::-1]
    
    for b in block:
    
        # last block might be smaller
        if bytes_read == n:
            break
        
        if b == "1":
            # normal ascii character
            byte = read(1)
            window.append(byte)
            fout.write(byte)
        else:
            # double non-ascii block
            # block: AB CD
            # window position = CAB + offset
            # data length = D
            # note that the prefix also contains the two letters before the given position
            byte = read(2).hex()
            wloc = hex2int(byte[2] + byte[0:2], 12) + woff # window location
            dlen = int(byte[3], 16) # data length

            for i in range(wloc-2, wloc+dlen+1):
                if i < 0:
                    next = b"\x20" # white space
                else:
                    next = window[i]
                fout.write(next)
                window.append(next)
                
    print(n, bytes_read)
                
    

f.close()
fout.close()
