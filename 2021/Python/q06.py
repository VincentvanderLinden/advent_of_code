import numpy as np
import math

with open('q06.in') as f: 
    src = [*map(int, f.read().split(','))]

fishies = np.array(src)

def the_faster_circle_of_live(fishies, cycles): 
    # Create an array of zeros as age
    age = np.zeros(9)
    #print(fishies)
    for fish in fishies: 
        age[fish] += 1
    for cycle in range(cycles) :
        # Reset any fish that gave birth to 6 (index 7 to account for roll)
        age[7] += age[0]
        # Shift array to the left
        age = np.roll(age, -1)
        ## Add number of zero fishies
    return age

print(f"Answer 1: {sum(the_faster_circle_of_live(fishies, 80))}")
print(f"Answer 2: {sum(the_faster_circle_of_live(fishies, 256))}")
