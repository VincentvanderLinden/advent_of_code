import os
#os.chdir('aoc')

with open('q03.in') as f:
    input = f.read().splitlines()
split_strings = []
#Create sets from first and second half strings
for line in input:
    half_split = int(len(line)/2)
    left_half = set(line[:half_split])
    right_half = set(line[half_split:])
    split_strings.append((left_half, right_half))

#Find matching letters by taking the intersection of the left and right split
matching_letters = []
for couple in split_strings:
    matching_letter = couple[0].intersection(couple[1])
    matching_letters.append(*matching_letter)

#Create scoring list for letters
letters = [*map(chr, range(97, 123))] + [*map(chr, range(65, 91))]
scoring_list = dict([*zip(letters, [*range(1,53)])])

#ANSWER PART 1
answer1 = sum([scoring_list[letter] for letter in matching_letters])
print(f"answer 1: {answer1}")

#Part two
#Split in groups of three
three_lines = [input[i:i + 3] for i in range(0, len(input), 3)]
#Create list of sets within the groups
sets = [[set(item) for item in group] for group in three_lines]
#Get the matching letter within each group of three
matching_letters = [set.intersection(*x) for x in sets]
#Calculate the score (using pop() to get the set value)
score = 0
for letter in matching_letters:
    score += scoring_list[letter.pop()]

#ANSWER PART 2
print(f"answer 2: {score}")

