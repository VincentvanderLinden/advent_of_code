import re

with open('q04.in') as f:
    input = f.read().splitlines()

assignment_pairs = [line.split(',') for line in input]

# Initialize answers
containing_pairs = 0
overlapping_pairs = 0

# Expensive solution checking all values, might be useful some day :)
for elf1, elf2 in assignment_pairs:
    # Extract numbers from the strings
    elf1_numbers = [int(num) for num in re.findall(r"\d+", elf1)]
    elf2_numbers = [int(num) for num in re.findall(r"\d+", elf2)]
    # Create range objects
    range1 = range(elf1_numbers[0], elf1_numbers[1]+1)
    range2 = range(elf2_numbers[0], elf2_numbers[1]+1)
    # Check if ALL numbers from the first range are in the second or vice versa
    if min([x in range1 for x in range2]) | min([x in range2 for x in range1]):
        containing_pairs += 1
    # Check if ANY numbers from the first range are in the second or vice versa
    if max([x in range1 for x in range2]) | max([x in range2 for x in range1]):
        overlapping_pairs += 1
#Answers
print(f"answer 1: {containing_pairs}")
print(f"answer 2: {overlapping_pairs}")

# Alternative faster way
containing_pairs = 0
overlapping_pairs = 0

for elf1, elf2 in assignment_pairs:
    # Extract start and end numbers from the strings
    elf1_start, elf1_end = [int(num) for num in re.findall(r"\d+", elf1)]
    elf2_start, elf2_end = [int(num) for num in re.findall(r"\d+", elf2)]
    # Check if pairs contain eachother by comparing starts and ends
    if (((elf1_start >= elf2_start) & (elf1_end <= elf2_end)) |
         (elf2_start >= elf1_start) & (elf2_end <= elf1_end)):
        containing_pairs += 1
    # Check overlapping_pairs by comparing the starts and ends of the ranges
    if any([elf2_start <= elf1_start <= elf2_end,
           elf2_start <= elf1_end <= elf2_end,
           elf1_start <= elf2_start <= elf1_end,
           elf1_start <= elf2_end <= elf1_end]):
        overlapping_pairs += 1

print(f"answer 1: {containing_pairs}")
print(f"answer 2: {overlapping_pairs}")



