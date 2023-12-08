with open('q03.in') as f: 
    input = f.read()


# Part 1
x, y = 0, 0
coords = set((x, y))

for i in input: 
    if i == '^': 
        y += 1 
    elif i == 'v': 
        y -= 1
    elif i == '>': 
        x += 1
    elif i == '<': 
        x -= 1
    coords.add((x, y))    

print(f"Answer 1: {len(coords)}")