with open('q02.in') as f:
    src = f.read().splitlines()

instructions = [line.split() for line in src]

horizontal = 0
depth = 0

for instruction in instructions: 
    direction, amount = instruction[0], int(instruction[1])
    if direction == 'forward':
        horizontal = horizontal + amount
    elif direction == 'up':
        depth = depth - amount
    elif direction == 'down':
        depth = depth + amount
        

print(f"Answer 1: {horizontal * depth}")

#Part two
aim = 0
horizontal = 0
depth = 0

for instruction in instructions: 
    direction, amount = instruction[0], int(instruction[1])
    if direction == 'forward':
        horizontal = horizontal + amount
        depth = depth + aim * amount
    elif direction == 'up':
        aim = aim - amount
    elif direction == 'down':
        aim = aim + amount

print(f"Answer 2: {horizontal * depth}")