import numpy as np

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

# Cycles and X start at 1 due to the nature of the instructions
cycle = 1
X = 1
signal_strength = 0

for instruction in instructions: 
    amount, cycles = instruction[0], instruction[1]
    for i in range(cycles): 
        # If it's the last cycle, up the X score
        if i == cycles - 1: 
            X += amount 
        # Increase cycle count
        cycle += 1
        # Add the score for every 20th, 60th, etc cycle    
        if (cycle - 20)%40 == 0: 
            signal_strength += cycle * X
    
print(f"Answer 1: The signal strength is {signal_strength}")

# Part 2
chararray = np.zeros((4,10), dtype='S1')
print(chararray)