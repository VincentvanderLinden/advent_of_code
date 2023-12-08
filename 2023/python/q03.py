with open('q03.in') as f:
    grid = f.read().splitlines()

def check_char_touch(grid, char_regex, row, col): 
    for r in range(max(0, row-1), min(row+2, len(grid))):
        for c in range(max(0, col-1), min(col+2, len(grid[0]))): 
            if re.match(char_regex, grid[r][c]) is not None:
                #grid[r][c] != '.' and not grid[r][c].isdigit(): 
                return True
    return False

nums = []

for row_ix, row in enumerate(grid): 
    number_tracker = False
    char_found = False
    number = ''

    for col_ix, col in enumerate(row): 
        if col.isdigit(): 
            number_tracker = True
            number += col
            if not char_found: 
                char_found = check_char_touch(grid, '[^\.\d]', row_ix, col_ix)
            
            # print if it's the last number in a row (and char is found)
            if col_ix == len(row) - 1 and char_found: 
                nums.append(number)
                number = ''
                number_tracker = False
                char_found = False

        else: 
            if number_tracker and char_found: 
                nums.append(number)
            number = ''
            number_tracker = False
            char_found = False

print(f'Answer 1: {sum(map(int, nums))}')

import re
from math import prod

ugh = {}
star_locations = []

# data collection
for row_ix, row in enumerate(grid): 
    stars = [(row_ix ,i) for i, x in enumerate(row) if x == '*']
    if stars: 
        for star in stars: 
            star_locations.append(star)
    numbers = [(m.start(), m.end(), int(m.group(0))) for m in re.finditer('\d+', row)]
    ugh[row_ix] = numbers
    check_number = check_char_touch(grid, '\d', row_ix, col_ix)

answer2 = 0

for star in star_locations: 
    print(f'star location: {star}')
    m = []
    for row in range(star[0]-1, star[0]+2): 
        r = ugh[row]
        for number in r: 
            print(number, star)
            if number[0]-1 <= star[1] <= number[1]: 
                print(f'number: {number}') 
                m.append(number[2])
    print(f'm: {m}')
    if len(m) == 2: 
        print(f'increasing answer with {prod(m)}')
        answer2 += prod(m)

print(answer2)
        
        