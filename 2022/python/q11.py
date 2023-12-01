import re
import math
from copy import deepcopy

# Open File
with open('q11.in') as file:
    src = file.read().split('\n\n')
# Seperate monkeys
monkeys = [line.split('\n') for line in src]
# Create the magnificent monkeytown as a list
monkeytown = []

# Evaluate input and put it into a list of monkeys with dicts of information
for idx, monkey in enumerate(monkeys):
    monkeytown.append({
        # Deque for popleft
        'name': idx,
        'items': [int(item) for item in re.findall(r"\d+", monkey[1])],
        'operation': monkey[2].split()[-3:],
        'test': int(re.findall(r"\d+", monkey[3])[0]),
        'if_true': int(*re.findall(r"\d+", monkey[4])),
        'if_false': int(*re.findall(r"\d+", monkey[5])),
        'no_of_inspects': 0,
    })


def monkey_business(monkeytown, part):
    # Calculate common divisor for part 2 to keep the value low
    common_divisor = math.prod([monkey['test'] for monkey in monkeytown])
    for monkey in monkeytown:
        while len(monkey['items']) > 0:
            monkey['no_of_inspects'] += 1
            # Replace operation (eg old * 19) with item_value * 19 and eval
            worry_level = eval(''.join(
                [*map(lambda x: x.replace('old', str(monkey['items'][0])), monkey['operation'])]))
            # Divide by 3
            if part == 1:
                worry_level = math.floor(worry_level / 3)
            # Keep the worry level low!
            if part == 2:
                if worry_level > common_divisor:
                    worry_level = worry_level % common_divisor
            # Check if it's divisible
            if worry_level % monkey['test'] == 0:
                # Throw the item to the if_true monkey and pop from list
                monkeytown[monkey['if_true']]['items'].append(worry_level)
                monkey['items'].pop(0)
            else:
                # Throw the item to the if_false monkey and pop from list
                monkeytown[monkey['if_false']]['items'].append(worry_level)
                monkey['items'].pop(0)


# Part 1:
# Run function 20 times
monkeytown_part1 = deepcopy(monkeytown)
for _ in range(20):
    monkey_business(monkeytown_part1, part=1)
# Multiply top two monkeys
answer = math.prod(sorted([monkey['no_of_inspects']
                   for monkey in monkeytown_part1])[-2:])
print(f"Answer 1: {answer}")


# Part 2:
monkeytown_part2 = deepcopy(monkeytown)
# Run function 10000 times
for _ in range(10000):
    monkey_business(monkeytown_part2, part=2)
# Multiply top two monkeys
answer = math.prod(sorted([monkey['no_of_inspects']
                   for monkey in monkeytown_part2])[-2:])
print(f"Answer 2: {answer}")
