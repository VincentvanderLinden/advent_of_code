with open('q10.in') as f: 
    src = f.read().splitlines()

open_char = {'(': 3, '[': 57, '{': 1197, '<': 25137}
close_char = {')': 3, ']': 57, '}': 1197, '>': 25137}
open_set = []
close_set = []
illegal_characters = []
for line in src: 
    for char in line: 
        if open_char.get(char) is not None: 
            open_set.append(open_char[char])
        if close_char.get(char) is not None: 
            if close_char[char] != open_set[-1]: 
                illegal_characters.append(char)
                break
            else:     
                # Add it to the close_set
                close_set.append(close_char[char])
                # Pop the open set
                open_set.pop()
      
print(f"Answer 1: {sum([close_char[i] for i in illegal_characters])}")

# Part two
open_char = {'(': 1, '[': 2, '{': 3, '<': 4}
close_char = {')': 1, ']': 2, '}': 3, '>': 4}
open_set = []
close_set = []
scores = []

for line in src: 
    open_set = []
    valid = True
    for char in line: 
        if open_char.get(char) is not None: 
            open_set.append(open_char[char])
        if close_char.get(char) is not None: 
            if close_char[char] != open_set[-1]: 
                # Corruption!
                valid = False
                break
            else:     
                open_set.pop()
    # If there is something left in the open set, calc score 
    if len(open_set) > 0 and valid: 
        total_score = 0
        for i in range(len(open_set)):
            total_score *= 5
            # Reverse the open set to generate close set
            total_score += [*reversed(open_set)][i]
        scores.append(total_score)
        
print(f"Answer 2: {sorted(scores)[int(len(scores)/2)]}")