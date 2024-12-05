import numpy as np
import re

with open('q04.in', 'r') as file:
        lines = file.readlines()
        array = [list(line.strip()) for line in lines]
        m = np.array(array)
    
pattern = '(?=XMAS|SAMX)'

def find_word(pat, l): 
    return len(re.findall(pat, ''.join(l)))
    
def get_all_diagonals(matrix):
    diagonals = []
    rows, cols = matrix.shape

    # Get main diagonals
    for offset in range(-rows + 1, cols):
        diagonals.append(matrix.diagonal(offset))

    # Get anti-diagonals
    flipped_matrix = np.fliplr(matrix)
    for offset in range(-rows + 1, cols):
        diagonals.append(flipped_matrix.diagonal(offset))

    return diagonals

res = 0


for horizontal in m: 
    res+=find_word(pattern, horizontal)

for vertical in np.rot90(m): 
    res+=find_word(pattern, vertical)

for diagonal in get_all_diagonals(m): 
    res+=find_word(pattern, diagonal)

print(f"Question 1: {res}")

res = 0

for row in range(len(m) - 2): 
    for col in range(len(m[0]) - 2): 
        if m[row, col] in ['M', 'S']: 
            # M . M 
            # . A . 
            # S . S
            lr = m[row, col] + m[row+1, col+1] + m[row+2, col+2]
            rl = m[row, col+2] + m[row+1, col+1] + m[row+2, col]
            if lr in ['MAS', 'SAM'] and rl in ['MAS', 'SAM']: 
                res+=1
                
print(f"Question 2: {res}")
    
