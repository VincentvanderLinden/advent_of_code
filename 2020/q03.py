import numpy as np
with open('q03.in') as f:
    src = f.read().splitlines()
forest = [[char for char in line] for line in src]

def move(forest, right, down): 
    trees = 0
    col = 0
    for idx, row in enumerate(forest):
        # Traverse the forest
        # index modulo down movement must be 0
        if(idx%down == 0):
            # Divide the index by the down movement and multiply by right movement
            col = int(idx/down*right) % len(forest[0])
            if(idx > 0 and forest[idx][col] == '#'):
                trees += 1
    return(trees)

print(f"Answer 1: {move(forest, 3, 1)}")

trees = move(forest, 1, 1)
for dir in [(3, 1), (5, 1), (7, 1), (1, 2)]:
    trees *= move(forest, dir[0], dir[1])
print(f"Answer 2: {trees}")


