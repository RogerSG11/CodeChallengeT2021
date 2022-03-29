# CHALLENGE 4 - LET'S BUILD MUSICAL SCALES


# AUXILIARY DATA

# Basic notes
notes = ["A", "B", "C", "D", "E", "F", "G"]

# Position of notes in the complete list
values = {
    "A": 0,
    "B": 2,
    "C": 3,
    "D": 5,
    "E": 7,
    "F": 8,
    "G": 10,
}


# MAIN

# Get number of cases
N = int(input())

for n in range(N):

    #Get input: root and steps (1 for semitone, 2 for tone)
    root = input()
    steps = [1 if x=='s' else 2 for x in input()]
    
    # Build scale of basic notes
    root_idx = notes.index(root[0])
    l = len(notes)
    basic = [notes[(i+root_idx)%l] for i in range(l)]
    basic.append(basic[0])
    
    # Start scale with root
    # b = basic value - 1, # = basic value + 1
    scale = [root]
    act = values[root[0]]
    if root[-1] == '#':
        act += 1
    elif root[-1] == 'b':
        act -= 1
    
    # Build scale by adding appropriate version of each basic note
    # Note that we might have to use e.g. E# even though it's not in the list
    for note, step in zip(basic[1:], steps):
        
        # Compare next value needed and value of next note to choose version
        next = (act + step)%12
        val = values[note]
        if next == val:
            scale.append(note)
        elif next == (val+1)%12:
            scale.append(note+"#")
        else:
            scale.append(note+"b")
        
        # Update current value
        act = next
        
    # In the end, scale[-1] == scale[0]
        
    # Print resulting scale as string
    print(f"Case #{n+1}: {''.join(scale)}")

