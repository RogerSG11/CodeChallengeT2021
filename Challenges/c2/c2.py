# CHALLENGE 2 - CATCH THEM ALL

# Number of cases
N = int(input())

for n in range(N):
    
    # Case description (P = #pokemon, R = #rows, C = #columns)
    P, R, C = [int(x) for x in input().split()]
    
    # Get list of pokemons and map (flattened to 1 line and converted to string)
    pokelist = []
    for _ in range(P):
        pokelist.append(input())
        
    pokemap = ""
    for _ in range(R):
        pokemap += "".join(input().split())
        
    
    # Iterate over list until no pokemon is left
    while pokelist:
        
        for poke in pokelist:
        
            # save size
            pokesize = len(pokemap)
        
            # Look for string and remove (left to right)
            pokemap = pokemap.replace(poke, "")
            
            # Look for string and remove (right to left)
            pokemap = pokemap.replace(poke[::-1], "")
        
            # Check if poke was replaced
            # In that case, remove poke from list
            if len(pokemap) != pokesize:
                pokelist.remove(poke)
        
    # Print remaining map
    print(f"Case #{n+1}: {pokemap}")
