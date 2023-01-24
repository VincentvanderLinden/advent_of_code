import re
import copy

with open('q05.in') as file:
    stack_input, instruction_input = file.read().split('\n\n')

#Split lines in every character starting from line position 1 in steps of 4
#(so 1, 5, 9, etc) 
stack_lines = [[line[i] for i in range(1, len(line), 4)] for line in stack_input.split('\n')]
#remove useless last line
stack_lines = stack_lines[:-1]
#Create stacks by zipping the list of lists
stacks = [*map(list, zip(*stack_lines))]
#Reverse the stacks
stacks = [stack[::-1] for stack in stacks]
#Remove empty boxes (they are not really there!
stacks = [[box for box in stack if box != ' '] for stack in stacks]

#Create deepcopys. Is this needed?
stack_result_1 = copy.deepcopy(stacks)
stack_result_2 = copy.deepcopy(stacks)

#Define box moving function
def move_boxes(stacks, source, target, amount):
    stacks[target - 1].extend(stacks[source - 1][-amount:])
    # Can't pop a full list, reset to empty list if needed
    if len(stacks[source - 1]) == amount:
        stacks[source - 1] = []
    # Otherwise pop the correct amount of boxes by deleting the indices
    else:
        del stacks[source - 1][-amount:]
    return(stacks)

for instruction in instruction_input.split('\n'):
    # Get amount, source, target from instructions
    amount, source, target = [int(i) for i in re.findall('\d+', instruction)]
    i = 1
    #Part 1: box per box
    while i <= amount:
        stack_result_1 = move_boxes(stack_result_1, source, target, 1)
        i += 1
    #Part 2: multiple boxes at the same time
    stack_result_2 = move_boxes(stack_result_2, source, target, amount)
    
#Join the last letters (top boxes)
answer1 = ''.join([x[-1] for x in stack_result_1])
answer2 = ''.join([x[-1] for x in stack_result_2])
print(f"answer1: {answer1}")
print(f"answer2: {answer2}")