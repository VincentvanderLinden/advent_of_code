import re
import numpy as np

with open('q13.in') as f: 
    rounds = f.read().split('\n\n')


total_price = 0

for round in rounds: 
    possibles = []
    a_x, a_y, b_x, b_y, price_x, price_y = map(int, re.findall(r'\d+', round))   
    
    for a in range(100): 
        for b in range(100): 
            x = a*a_x + b*b_x
            y = a*a_y + b*b_y
    
            if x == price_x and y == price_y: 
                possibles.append(a*3 + b)
    price = min(possibles) if len(possibles) > 0 else 0    
    total_price += price  
    

print(f"Answer 1: {total_price}")

# Part 2 LEZGO

total_price = 0

# I R 2 stupid
