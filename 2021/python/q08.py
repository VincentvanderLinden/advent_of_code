import re
with open('q08.in') as f:
    src = f.read().splitlines()

# Part 1

appearances = 0
for line in src: 
    # Get part after | and split by space
    output = re.findall(r"(?<=\| ).*", line)[0].split(' ')
    # Count the outputs with lenghts 2, 3, 4, 7
    output_lengths = len([x for x in output if len(x) in [2, 3, 4, 7]])
    # Add the lenghts to the final result
    appearances += output_lengths
print(f"Answer 1: {appearances}")

# Part 2 -- screw this
# len = value
# 2 = 1
# 3 = 7
# 4 = 4
# 7 = 8
# 5 = 2, 3, 5
# 6 = 0, 6, 9

# Easy to translate numbers:
easy_ones = {2: 1, 3: 7, 4: 4, 7: 8}
output_sum = 0    

for line in src: 
    # Get part before | and split by space
    signal_patterns = re.findall(r".*(?= \|)", line)[0].split(' ')
    # Collect the outputs with lengths 2, 3, 4, 7 into a dict for translation
    output_keys = {len(x): x for x in signal_patterns if len(x) in [2, 3, 4, 7]}
    translation = dict()
    
    # Parse output
    for seq in signal_patterns: 
        seq_chars = [char for char in seq]
    # Check if it's and easy length, we know the translation
        if(len(seq) in easy_ones.keys()):
            translation[seq] = easy_ones[len(seq)]
        # Five characters mean a 0, 6, 9
        elif len(seq) == 6:
            # If it has the same chars as 4 (output_keys[4]), it must be a nine
            if all(char in seq_chars for char in [x for x in output_keys[4]]):
                translation[seq] = 9
            # If it has the same chars as 1 (output_keys[2]), it must be a zero    
            elif all(char in seq_chars for char in [x for x in output_keys[2]]):
               translation[seq] = 0
            # Else it must be a six
            else: 
                translation[seq] = 6
        # Five characters mean a 2, 3, or 5
        elif len(seq) == 5:
            # If it has the same chars as 1 (output_keys[2]), it must be a three
            if all(char in seq_chars for char in [x for x in output_keys[2]]):
                translation[seq] = 3
            # If it has the same chars as 4 (output_keys[4] EXCLUDING 1 (output_keys[2])), it must be a five    
            elif all(char in seq_chars for char in [x for x in output_keys[4] 
                    if x not in [y for y in output_keys[2]]]):
                translation[seq] = 5
            # Else it must be a two
            else: 
                translation[seq] = 2

    # Get part after | and split by space
    output = re.findall(r"(?<=\| ).*", line)[0].split(' ')
    output_numbers = []

    for seq in output: 
        seq_chars = [char for char in seq]
        for key, value in translation.items():
            # Fuzzy match
            if all(char in [x for x in key] for char in seq_chars) and len(key) == len(seq_chars): 
                output_numbers.append(str(value))

    output_sum += int(''.join(output_numbers))

print(f"Answer 2: {output_sum}")

