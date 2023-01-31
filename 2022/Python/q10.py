import numpy as np
import math

with open('q10.in') as file:
    input = file.read().splitlines()
# Create instruction list for better handling: amount of addx (0 for noop) and amount of cycles (1 or 2)
# Less logic needed in the following loop(s) by doing it this way
instructions = []
for line in input: 
    if line == 'noop':
        # Put amount and number of cycles
        instructions.append((0, 1))
    else:
        instructions.append((int(line.split(' ')[1]), 2))

# Initialize variables. Cycles and X start at 1 due to the nature of the instructions
cycle = 1
X = 1
signal_strength = 0
# For part two: create a ndarray(6, 40) filled with dots:
# Allow numpy to actually show all characters in the console
np.set_printoptions(linewidth=10000000)
# Create a ndarray(6, 40) filled with dots:
pixels = np.full((6, 40), '.',  dtype='U1')

for instruction in instructions:
    amount, cycles = instruction[0], instruction[1]
    for i in range(cycles):
        # Part two: drawing pixels
        # Check if the cycle is aligned with three pixels between X and X + 3
        if cycle % 40 in range(X, X+3):
            # If so, set the position in the ndarray to %, using floor and mod to get the right row and column
            pixels[math.floor(cycle/40), cycle % 40] = '#'
        # If it's the last cycle, up the X score
        if i == cycles - 1:
            X += amount
        # Increase cycle count
        cycle += 1
        # Add the score for every 20th, 60th, etc. cycle
        if (cycle - 20) % 40 == 0:
            signal_strength += cycle * X

print(f"Answer 1: The signal strength is {signal_strength}")
print(f"Answer 2: The CRT screen is showing this\n {pixels}")
