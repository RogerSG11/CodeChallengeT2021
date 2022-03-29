# CHALLENGE 18 - BIT SAVER

import tarfile

# BINARY TREE TO STORE ENCODING
class Node:

    def __init__(self, freq, symbol, left=None, right=None, depth=0):
    
        self.freq = freq # frequency of command
        self.symbol = symbol # name of command
        self.left = left # Left child
        self.right = right # right child
        self.huff = '' # tree direction (0/1)
        self.depth = depth # pseudo-depth in the tree. 0 for leaves. Used to balance tree.


# GENERATE HUFFMAN TREE
def huffmanCoding(commands):
    
    # list of unused, newly generated nodes
    nodes = [Node(freq, cmd) for cmd, freq in commands.items()]
    
    # In the case where we only have one node, it itself is the tree root
    if len(nodes) == 1:
        node = nodes[0]
        node.huff = 0
        return node
    
    while len(nodes) > 1:
        
        # sort nodes in ascending order based on frequency (min payload length)
        # If equal frequency, then use pseudo-depth to balance tree (min diff)
        nodes = sorted(nodes, key = lambda x : (x.freq, x.depth))
        
        # pick 2 smallest nodes (and remove from list)
        left = nodes.pop(0)
        right = nodes.pop(0)
        
        # assign directional value to these nodes
        left.huff = 0
        right.huff = 1
        
        # combine the 2 smallest nodes to create new node as their parent
        newFreq = left.freq + right.freq
        newDepth = max(left.depth, right.depth) + 1 # MAX OR MIN??
        newNode = Node(newFreq, left.symbol + right.symbol, left, right, newDepth)
        
        # add parent to list of nodes
        nodes.append(newNode)
        
    # return root of tree
    return nodes[0]
    

# PRINT HUFFMAN CODES (helper function)
def printNodes(node, val=''):
    # huffman code for current node
    newVal = val + str(node.huff)
  
    # if node is not an edge node
    # then traverse inside it
    if(node.left):
        printNodes(node.left, newVal)
    if(node.right):
        printNodes(node.right, newVal)
  
        # if node is edge node then
        # display its huffman code
    if(not node.left and not node.right):
        print(f"{node.symbol} -> {newVal} x {node.freq}")
        

# Get huffman value for all nodes
# Initial call with node = root and codes = {}
def huffmanValues(node, codes, val=''):
    
    # huffman code for current node
    newVal = val + str(node.huff)
    
    # if node is not a leaf, then traverse inside it
    if (node.left):
        huffmanValues(node.left, codes, newVal)
    if (node.right):
        huffmanValues(node.right, codes, newVal)
        
    # if node is leaf, store code
    if not node.left and not node.right:
        codes[node.symbol] = str(newVal)


# get size of payload
def calculateMetrics(C, commands, codes):
    size = 2*C # 2 argument bits for every instruction
    minlen = float('inf')
    maxlen = 0
    for cmd, freq in commands.items():
        n = len(codes[cmd])
        size += freq*n
        if n > maxlen:
            maxlen = n
        if n < minlen:
            minlen = n
    return size, maxlen - minlen
    

# MAIN

# Step 1: read data from tar.gz
name = "submit"
filename = f"bit-saver-input-{name}.tar.gz"

tar = tarfile.open(filename)
f = tar.extractfile("input0")
tarline = lambda f : f.readline().decode().strip()
#tarline = lambda f : input()

N = int(tarline(f))

for n in range(N):

    # Step 2: get data
    # We need to know the frequency of each command
    # We know all arguments have 2 bits and appear once every line
    
    commands = {}

    C = int(tarline(f))
    for _ in range(C):
        
        cmd = tarline(f).split()[0]
        if cmd not in commands:
            commands[cmd] = 1
        else:
            commands[cmd] += 1
            
    # Step 3: get minimum length - HUFFMAN CODING
    root = huffmanCoding(commands)
    codes = {}
    huffmanValues(root, codes)
    length, diff = calculateMetrics(C, commands, codes)
    
    print(f"Case #{n+1}: {length}, {diff}")
    
tar.close()
