# CHALLENGE 5 - INVICTUS

# After performing hexdump, notice sequences b'\xf3\xa0\x81\xXX'
# These correspond to utf-8 encoded characters
# Afterwards there's some sort of Caesar's cipher

fin = open("Invictus.txt", "rb")

bytelist = [] # list of all non-ascii bytes

byte = fin.read(1)
while byte != b"":
    
    if byte == b"\xf3":
        aux = byte
        aux += fin.read(3)
        #print(aux)
        
        aux = aux.decode('utf-8')
        aux = ord(aux)
        aux = chr(aux - 917550)
        print(aux, end="")
    
    byte = fin.read(1)
        
fin.close()

print()
