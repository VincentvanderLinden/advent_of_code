from copy import deepcopy

with open('q08.in') as f:
    src = f.read().splitlines()

program = [[line.split(' ')[0], int(line.split(' ')[1])] for line in src]


def process_line(program, execution_state):
    # current_line, visited_lines, accumulator
    # Add current line to list of visited lines
    execution_state['visited_lines'].append(execution_state['current_line'])
    operation, amount = program[execution_state['current_line']]
    # Run Program
    if operation == 'nop': 
        # Go to next line
        execution_state['current_line']  += 1
    elif operation == 'acc': 
        # Add amount to accumulator and go to next line
        execution_state['accumulator']  += int(amount)
        execution_state['current_line']  += 1
    elif operation == 'jmp': 
        # Jump 
        execution_state['current_line'] += int(amount)
    return (execution_state)

#Initialize execution state
execution_state = {'current_line' : 0, 
                   'visited_lines' : [], 
                   'accumulator': 0}
# Initialize infinite loop recognizer
infinite_loop = False

# Loop through rest of program
while not infinite_loop:
    if execution_state['current_line'] in execution_state['visited_lines']: 
        infinite_loop = True
        print("Answer 1:", execution_state['accumulator'])
    else: 
        process_line(program, execution_state)


## Part Two

#Initialize execution state
execution_state = {'current_line' : 0, 
                   'visited_lines' : [], 
                   'accumulator': 0}

# Initialize infinite loop recognizer
end_of_program = False
# Identify jmp and nop positions
jmp_positions = [(idx, line) for idx, line in enumerate(program) if line[0] == 'jmp']
nop_positions = [(idx, line) for idx, line in enumerate(program) if line[0] == 'nop']

# Make a deepcopy so we can reset it
running_program = deepcopy(program)

# Pick a position type and substitution
positions = nop_positions
substitute = 'jmp'

# Loop through rest of program
while not end_of_program:
    if execution_state['current_line'] == len(running_program): 
        print('Answer 2:', execution_state['accumulator'])
        end_of_program = True
    elif execution_state['current_line'] in execution_state['visited_lines']: 
        # Infinite loop reached, change program and reset execution state
        if len(positions) == 0:
            print('tried all nop positions, switching to jmp') 
            positions = jmp_positions
            substitute = 'nop'
            continue
        else: 
            # reset program
            running_program = deepcopy(program)
            # change 1 position
            running_program[positions[0][0]][0] = substitute
            # remove it from list of positions
            positions.pop(0)
            # reset execution state
            execution_state = { 'current_line' : 0, 
                                'visited_lines' : [], 
                                'accumulator': 0}
            process_line(running_program, execution_state)
    else: 
        process_line(running_program, execution_state)