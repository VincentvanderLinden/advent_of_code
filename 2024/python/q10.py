import numpy as np
with open('q10.in') as f: 
    m =[list(n.strip()) for n in f.readlines()]
    for r in range(len(m)): 
        for c in range(len(m[0])): 
            if m[r][c] == '.': 
                m[r][c] = '-1'
    m = np.array(m).astype(np.int) 



trailheads = []
for row in range(len(m)): 
    for col in range(len(m[0])): 
        if m[row][col] == 0: 
            trailheads.append((row, col))

DIRS = [(0, 1), (1, 0), (-1, 0), (0, -1)]
VISITED = set()

def check_adj(route, cur_r, cur_c, cur_val): 
    
    route += (cur_r, cur_c)
    
    if cur_val == 9: 
        VISITED.add(route)
        return
    else: 
        any_found = False
        for d in DIRS: 
            r, c = d
            if cur_r + r >= 0 and cur_r + r < len(m) and cur_c + c >= 0 and cur_c + c < len(m[0]):
                if m[cur_r + r, cur_c + c] == cur_val + 1: 
                    check_adj(route, cur_r + r, cur_c + c, cur_val + 1)
                    any_found = True
        if not any_found: 
            return

     
for t in trailheads: 
    r,c = t
    check_adj((), r, c, m[r, c])

end_points_hit = set([(x[:2], x[-2:]) for x in VISITED])

print(f"Answer 1: {len(end_points_hit)}")
print(f"Answer 2: {len(VISITED)}")

