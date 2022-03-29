# CHALLENGE 14 - SEND + MORE = MONEY

import re
import sys
from itertools import permutations

# Get all possible solutions via bruteforce
# https://www.cmi.ac.in/~madhavan/courses/prog2-2011/docs/diveintopython3/advanced-iterators.html
def solve(puzzle):

    # Find all words (operands and result)
    words = re.findall('[A-Z]+', puzzle.upper())
    
    # Find all unique characters
    unique_characters = set(''.join(words))
    
    # Check we don't have too many letters
    if len(unique_characters) > 10:
        return []
        
    # Get first letter of each word
    first_characters = {word[0] for word in words}
    n = len(first_characters)
    
    # List all characters, with the first letters at the start
    sorted_characters = ''.join(first_characters) + ''.join(unique_characters - first_characters)
    
    # Get unicode value for letters and digit, and store the digit zero
    characters = tuple(ord(c) for c in sorted_characters)
    digits = tuple(ord(d) for d in '0123456789')
    zero = digits[0]
    
    # Convert "=" to "==" for proper evaluation
    puzzle = re.sub("=", "==", puzzle)
    
    # Array to store all solutions
    solutions = []
    
    # Check all possible assignations
    # Could be parallelized since each permutation is independent
    for guess in permutations(digits, len(characters)):
        # Check that number does not start in zero
        if zero not in guess[:n]:
        
            # Change letters for their numeric value
            # Letter/value need to be their respective unicode value
            equation = puzzle.translate(dict(zip(characters, guess)))

            # Evaluate equation
            # If true store solution (and recover original form of "=")
            if eval(equation):
                equation = re.sub("==", "=", equation)
                solutions.append(equation)
                
    return solutions

# MAIN

N = int(input())
for n in range(N):

    # Checkpoint for execution when printing to file
    print(f"Case {n+1} of {N}", file = sys.stderr)
    
    puzzle = input()
    solutions = solve(puzzle)
    
    if not solutions:
        # no solution
        print(f"Case #{n+1}: IMPOSSIBLE")
    else:
        print(f"Case #{n+1}: {';'.join(sorted(solutions))}")
