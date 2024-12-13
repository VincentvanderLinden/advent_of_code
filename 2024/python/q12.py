import utils
import numpy as np

import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull

inp = utils.read_matrix_from_file('q12.in', to_int=False, to_numpy=False)

SEEN = set()
PERIMETERS = {}

def find_adjacent_cells(inp: np.array, coords: tuple, garden_cells: list) -> list:

    dirs = ((-1,0), (1, 0), (0, -1), (0, 1)) 
    r, c = coords

    for d in dirs: 
        # Determine next cells
        r_next, c_next = r + d[0], c + d[1]
        
        # If possible:  
        if 0 <= r_next < len(inp) and 0 <= c_next < len(inp[0]) and inp[r_next][c_next] == inp[r][c]: 
            if (r_next, c_next) in SEEN: 
                continue
            else: 
                SEEN.add((r_next, c_next))
                garden_cells.append((r_next, c_next))        
                find_adjacent_cells(inp, (r_next, c_next), garden_cells)
    
    return garden_cells
                

def count_corners(cells: list) -> int:
    
    sides = 0
   
    # Check in all directions and determine if there is a corner
    for c in cells: 
        n, s, e, w = (c[0]-1, c[1]), (c[0]+1, c[1]), (c[0], c[1]+1), (c[0], c[1]-1)
        nw, sw, ne, se = (c[0]-1, c[1]-1), (c[0]+1, c[1]-1), (c[0]-1, c[1]+1), (c[0]+1, c[1]+1)
        
        # Outer corners
        sides += n not in cells and w not in cells
        sides += s not in cells and w not in cells
        sides += n not in cells and e not in cells
        sides += s not in cells and e not in cells
        # Inner corners
        sides += n in cells and w in cells and nw not in cells
        sides += s in cells and w in cells and sw not in cells
        sides += n in cells and e in cells and ne not in cells
        sides += s in cells and e in cells and se not in cells
        
    return sides


def calculate_price(garden: tuple, part=1) -> int: 
    multiplier = 0
    dirs = ((-1,0), (1, 0), (0, -1), (0, 1)) 
    area = garden[1].get('garden_size')
    if part == 1: 
        for cell in garden[1].get('garden_cells'): 
            perimeter = 4
            for d in dirs: 
                if (cell[0] + d[0], cell[1] + d[1]) in garden[1].get('garden_cells'):
                    multiplier -= 1
            multiplier += perimeter        
    elif part == 2: 
        
        multiplier += count_corners(garden[1].get('garden_cells'))
           
    return area*multiplier





GARDENS = {}
for r in range(len(inp)): 
    for c in range(len(inp[0])): 
        if (r, c) in SEEN: 
            continue
        else: 
            SEEN.add((r, c)) 
            garden = find_adjacent_cells(inp, (r, c), [])
            GARDENS[(r, c)] = {'starting_point': (r, c), 
                               'letter': inp[r][c],
                               'garden_cells': [(r, c)] + garden,                               
                               'garden_size' : len([(r, c)] + garden)
                        }
            
res1 = 0      
res2 = 0
for garden in GARDENS.items(): 
    res1 += calculate_price(garden, part=1)
    res2 += calculate_price(garden, part=2)

print(f"Answer 1: {res1}")
print(f"Answer 2: {res2}")
