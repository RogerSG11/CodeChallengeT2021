# CHALLENGE 13 - FIND THE NEW EARTH


# SCRIPT USED TO GET NON-ASCII ELEMENTS

with open("here-is-the-position", "rb") as f:

    byte = f.read(1)
    while byte != b"":
    
        #print(byte)
    
        if byte == b"\xe2":
            
            aux = byte
            aux += f.read(2)
            
            print(aux)
        
        byte = f.read(1)
        

# SOLUTION STEPS
'''
 
    1. Decipher hint with caesar's cipher to obtain 'user:password'
    2. Use found credentials to access the linked website
    3. Download file. It's a hexdump. Get binary with
        $ xxd -r here-is-the-position here-is-the-position.gz
    4. New file is gzip compressed data (that's why we added the extension in output in step 3).
       Decompress with
        $ gunzip here-is-the-position.gz
    5. We get an UTF-8 encoded text file with some text from LoR.
       Text contains only 3 non-ascii elements. List all of them using script above.
    6. Remove element ending in \x99 since it's just an apostrophe.
       Remaining elements correspond to unicode characters ZWSP and ZWNJ
    7. Perform steganography with zero-width characters on the file
       Use e.g. the following website, choosing only the two given characters:
        https://330k.github.io/misc_tools/unicode_steganography.html
    8. Download obtained binary file and output content with "cat" command
       THE DESIRED 15-DIGIT STRING IS FOUND
'''
