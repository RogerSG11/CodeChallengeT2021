# CHALLENGE 10 - PERDIUETES

from scapy.all import *

capture = rdpcap("icmps.pcap")
ping_data = b""

data = []

for packet in capture:
   data.append((packet.seq, packet.load))
    
data = sorted(data, key = lambda x : x[0])

for x, y in data:
    print(y.hex(), end=" ")
print() 

# 1. Get the packets and order by sequence number
# 2. Extract the last byte (packet data) in hex
# 3. Convert from Hex to see its an image, and therefore convert to image
#   https://gchq.github.io/CyberChef/#recipe=From_Hex('Space')Render_Image('Raw')
# 4. Scan QR code to obtain password
