with open('q01.in') as f:
    txt = f.read()

# Part 1
print(f"Answer 1: {txt.count('(') - txt.count(')')}")

# Part 2
floor = 0

for ix, char in enumerate(txt): 
    if char == '(': 
        floor += 1
    else: floor -= 1
    if floor < 0: 
        print(f"Answer 2: {ix + 1}")
        break