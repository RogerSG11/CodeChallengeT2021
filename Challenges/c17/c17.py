# CHALLENGE 17 - SUPPER DIGGER BROS AND THE BULLDOZER OF INFINITE BUCKETS

# Idea
# Calculate grundy number for each pile: G(Vi) = Vi mod 3
# Calculate grundy number for the hole system (Sprague-Grundy Theorem): G = XOR G(Vi)
# If G != 0, first player wins. Else second player wins.

T = int(input())

for t in range(T):

    N = int(input())
    volumes = [int(x) for x in input().split()]
    
    G = volumes[0] % 3
    for v in volumes[1:]:
        Gi = v % 3
        G = G ^ Gi
        
    winner = "Alberto" if G == 0 else "Edu"
    print(f"Case #{t+1}: {winner}")
