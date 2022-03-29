# CHALLENGE 3 - THE NIGHT OF THE HUNTER


# Get dictionary of values from dictionary
def getValuesDict(word1, word2, values):
    
    return eval(values)
    
    
# Get dictionary of values from list of tuples
def getValuesTuple(word1, word2, values):
    
    return {x: y for x, y in eval(values)}
    
 
# Get dictionary of values from list of assignments
def getValuesAssign(word1, word2, values):
    
    # Separate all assignments
    assigns = values.split(",")
    
    # Build dict
    vals_dict = {}
    
    for assign in assigns:
        letter, val = assign.split("=")
        val = eval(val) # We could have fractions
        vals_dict[letter] = val
        
    return vals_dict        
    
    
# Get winner, values is a dict with letter as keys
def getWinner(word1, word2, values):

    res1 = sum([values[x] for x in word1])
    res2 = sum([values[x] for x in word2])
  
    if res1 == res2:
        return "-"
    return word1 if res1 > res2 else word2


# MAIN

# Number of cases
N = int(input())

for n in range(N):

    # Get input
    words, values = input().split("|")
    word1, word2 = words.split("-")
    
    # Values can be given as a dictionary, list of tuples or list of assignments
    dict_values = {}
    if values[0] == '{':
        dict_values = getValuesDict(word1, word2, values)
    elif values[0] == '[':
        dict_values = getValuesTuple(word1, word2, values)
    else:
        dict_values = getValuesAssign(word1, word2, values)
        
    winner = getWinner(word1, word2, dict_values)
        
    print(f"Case #{n+1}: {winner}")
