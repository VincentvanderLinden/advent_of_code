import numpy as np
from collections import deque
with open('q08.in') as f: 
    m =[list(n.strip()) for n in f.readlines()]
    m = np.array(m)

ANTENNAE = set()
ANTENNAE_PLACED = set()

for r in range(len(m)): 
    for c in range(len(m[0])): 
        if m[r][c] != '.': 
            coords = (m[r][c], r, c)
            ANTENNAE.add(coords)

for a in ANTENNAE: 
    v, r, c = a
    other_a = [x for x in ANTENNAE if x[0] == v and x[1] != r and x[2] != c]
    for oa in other_a: 
        dist_y = r - oa[1]
        dist_x = c - oa[2]
        if 0 <= r + dist_y <= len(m) -1 and 0 <= c + dist_x <= len(m[0]) - 1: 
            ANTENNAE_PLACED.add((r + dist_y, c + dist_x))

print(f"{ANTENNAE_PLACED} \nAnswer 1: {len(ANTENNAE_PLACED)}")   



ANTENNAE_PLACED = set()

for a in ANTENNAE: 
    v, r, c = a
    other_a = [x for x in ANTENNAE if x[0] == v and x[1] != r and x[2] != c]
   
for oa in other_a: 
        dist_y = r - oa[1]
        dist_x = c - oa[2]
        i = 0
        while 0 <= r + dist_y*i <= len(m) - 1 and 0 <= c + dist_x*i <= len(m[0]) - 1: 
            ANTENNAE_PLACED.add((r + dist_y*i, c + dist_x*i))
            i+=1

print(f"Answer 2: {len(ANTENNAE_PLACED)}")   
