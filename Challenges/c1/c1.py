# CHALLENGE 1 - ROLL THE DICE!

# Get number of cases
N = int(input())

for n in range(N):
    
    # Dice sum by first player
    dice = sum([int(x) for x in input().split(":")])
    
    # Minimum score by player 2
    minsc = dice + 1
    
    # Print minimum score
    # If player 2 can't win (minsc > 12) print "-" 
    print(f"Case #{n+1}: {minsc if minsc <= 12 else '-'}")
   
