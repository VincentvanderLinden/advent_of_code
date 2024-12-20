import numpy as np
from time import sleep


with open('q15.in') as f:
    warehouse, instructions = f.read().split('\n\n')

wh_raw = [list(line) for line in warehouse.split('\n')]
instructions = instructions.replace('\n', '')
            
class Warehouse: 
    def __init__(self, wh: list[list]): 
        self.wh = wh
    
    def __repr__(self): 
        new_line = '\n'
        return f"{new_line.join(''.join(row) for row in self.wh)}"
        
    def __getitem__(self, row) -> list:
        return self.wh[row]
      
    def __len__(self): 
        return len(self.wh)
    
    def find_robot(self, robot_sign: str = '@') -> tuple:
        for row in range(len(self.wh)):
            for col in range(len(self.wh[0])): 
                if self.wh[row][col] == robot_sign:
                    return (row, col)
    
    
class Robot: 
    
    D = {'<': [0, -1], 
         '>': [0, 1],
         '^': [-1, 0], 
         'v': [1, 0]}
    
    def __init__(self, name: str, wh: np.array, starting_point: tuple, robot_sign: str = '@'): 
        self.name = name
        self.coordinates = starting_point
        self.wh = wh
        self.robot_sign = robot_sign
        
    def __repr__(self): 
        icon = '😸' if self.name.lower() in ['dana', 'poes', 'poeskoes'] else '🤖'
        return f"{icon} {self.name} is at {self.coordinates}"
    
    def transform_list(self, l: list, pos: int, reversed: bool = False) -> list: 
        
        if '.' in l[pos:pos + l[pos:].index('#')]: 
            l = l[:]
            first_space = pos + l[pos:].index('.')
            l.pop(first_space)
            l.insert(pos, '.')
            if reversed: 
                l = l[::-1]
            
        return l
             
    def move(self, d: str): 
        
        if d not in self.D: 
            raise ValueError(f'Invalid direction: {d}')
        
        r, c = self.coordinates
        next_r = r + self.D.get(d)[0]
        next_c = c + self.D.get(d)[1]

        # Wall 
        if self.wh[next_r][next_c] == '#': pass
        
        # Box
        elif self.wh[next_r][next_c] in ['O', '[', ']']: 

            if d == '>': 
                l = self.wh[r]
                new_l = self.transform_list(l=l, pos=c)
                if l != new_l: 
                    for ix, x in enumerate(new_l): 
                        self.wh[r][ix] = x  
                    self.coordinates = r, c+1
            
            elif d == '<': 
                l = self.wh[r][::-1]
                pos = len(self.wh[r]) - c - 1
                new_l = self.transform_list(l=l, pos=pos, reversed=True)
                
                if l != new_l: 
                    for ix, x in enumerate(new_l): 
                        self.wh[r][ix] = x  
                    self.coordinates = r, c-1
                
            elif d == 'v': 
                l = [row[c] for row in self.wh]
                new_l = self.transform_list(l=l, pos=r)
                l2 = None
                new_l2 = None
                col2move = None
                if self.wh[r+1][c] in ['[', ']']: 
                    # find bottom edges
                    
                    
                    col2move = c + 1
                    l2 = [row[col2move] for row in self.wh]
                    new_l2 = self.transform_list(l=l2, pos=r)
                
                if self.wh[r+1][c] == ']': 
                    col2move = c - 1
                    l2 = [row[col2move] for row in self.wh]
                    new_l2 = self.transform_list(l=l2, pos=r)
                    
                if (l != new_l and l2 is None) or (l != new_l and l2 != new_l2): 
                    for ix, x in enumerate(new_l): 
                        self.wh[ix][c] = x  
                    if new_l2 is not None: 
                        for ix, x in enumerate(new_l): 
                            self.wh[ix][col2move] = x 
                    self.coordinates = r+1, c   
                     
            elif d == '^': 
                l = [row[c] for row in self.wh][::-1]
                pos = len(self.wh) - r - 1               
                new_l = self.transform_list(l=l, pos=pos, reversed=True)
                #new_l2 = 
                
                if l != new_l: 
                    for ix, x in enumerate(new_l): 
                        self.wh[ix][c] = x  
                    self.coordinates = r-1, c   
            
        else: 
            wh[r][c] = '.'
            wh[next_r][next_c] = self.robot_sign
            self.coordinates = next_r, next_c

            
wh = Warehouse(wh_raw)
robot = Robot(name='Dana', wh = wh, starting_point=wh.find_robot())


for i in instructions: 
    robot.move(i)

p1 = 0 

for i in range(len(wh)): 
    for j in range(len(wh[0])): 
        if wh[i][j] == 'O': 
            p1 += 100*i + j

print(f"Answer 1: {p1}")


# with open('q15.in') as f:
#     warehouse, instructions = f.read().split('\n\n')

# wh_raw = [list(line) for line in warehouse.split('\n')]
# instructions = instructions.replace('\n', '')

# wh = Warehouse(wh_raw)

# FAT_WAREHOUSE = []

# for row in wh: 
#     r = []
#     for col in row: 
#         if col == '#': 
#             r += ["#"] * 2
#         elif col == 'O': 
#             r += ['[', ']']
#         elif col == '.': 
#             r += ['.'] * 2
#         elif col == '@': 
#             r += ['@', '.']
#     FAT_WAREHOUSE.append(r)      

# wh = Warehouse(FAT_WAREHOUSE)
# robot = Robot(name='Dana', wh=wh, starting_point=wh.find_robot())

# j = 0
# for i in instructions[:6]: 
#     print(f"Step {j}\n{i}")
#     robot.move(i)
#     print(wh)
#     j += 1


# p2 = 0 

# for i in range(len(wh)): 
#     for j in range(len(wh[0])): 
#         if wh[i][j] == 'O': 
#             p2 += 100*i + j

# print(f"Answer 2: {p2}")