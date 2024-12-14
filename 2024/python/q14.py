import re
import numpy as np
from math import prod
import sys
from collections import Counter
np.set_printoptions(threshold=sys.maxsize)

def calc_pos(s:int, ds: int , limit:int) -> int: 
    new_pos = s
    if s + ds < 0: 
        new_pos = limit + (s + ds)
    elif s + ds >= limit: 
        new_pos = (s + ds) - limit 
    else: 
        new_pos += ds
    return new_pos

def move(x: int, 
         y: int, 
         dx: int, 
         dy: int, 
         area_width: int, 
         area_height: int, 
         steps: int) -> tuple: 

    new_pos_x = calc_pos(s=x, ds=(dx*steps)%area_width, limit=area_width)
    new_pos_y = calc_pos(s=y, ds=(dy*steps)%area_height, limit=area_height)  

    return new_pos_x, new_pos_y



def calculate_position_after_n_steps(robots, 
                                     area_width: int, 
                                     area_height: int, 
                                     steps: int) -> list:
    robot_locations = []
    for robot in robots: 
        x, y, dx, dy = map(int, robot)
        x, y = move(x, y ,dx, dy, 
                    area_width=area_width, 
                    area_height=area_height, 
                    steps=steps)
        robot_locations.append((x, y))
        
    return robot_locations
    
    
def calculate_quadrants(area_width: int, area_height: int, robot_locations: list) -> dict(): 
    q1 = len([l for l in robot_locations if l[0] < area_width//2 and l[1] < area_height//2])
    q2 = len([l for l in robot_locations if l[0] > area_width//2 and l[1] < area_height//2])
    q3 = len([l for l in robot_locations if l[0] < area_width//2 and l[1] > area_height//2])
    q4 = len([l for l in robot_locations if l[0] > area_width//2 and l[1] > area_height//2])
    return {'q1': q1, 
            'q2': q2, 
            'q3': q3, 
            'q4': q4,}

def plot_locs(locs, area_width: int, area_height: int): 
    n = np.array([[' '] * (area_width)] * (area_height))
    for l in locs: 
        n[l[1]][l[0]] = str(int(n[l[1]][l[0]])+1) if n[l[1]][l[0]] != ' ' else '1'  
    return n


# Initialize and run

robots = []

with open('q14.in') as f: 
    for line in f.readlines(): 
        robots.append(re.findall(r'-?\d+', line))
        
locs = []
STEPS = 100
W = 101
H = 103

robot_locations = calculate_position_after_n_steps(robots,
                                                   area_width=W, 
                                                   area_height=H, 
                                                   steps=STEPS)


quadrants = calculate_quadrants(area_width=W, 
                                area_height=H, 
                                robot_locations=robot_locations)

print(f"Answer 1: {prod(quadrants.values())}")

for n in range(1000000): 

    robot_locations = calculate_position_after_n_steps(robots,
                                                       area_width=W, 
                                                       area_height=H, 
                                                       steps=n)
    x = Counter([l[1] for l in robot_locations])
    y = Counter([l[0] for l in robot_locations])
    
    if 19 in x.values() and 19 in y.values(): 
        print('_'* W)
        for l in plot_locs(robot_locations, area_height=H, area_width=W): 
            print(''.join(l))
        print('_'* W)
        print(f"Answer 2: {n}")
        break
