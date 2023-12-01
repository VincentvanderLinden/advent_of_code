# Open file and split on double returns
with open('q01.in') as f:
    src = f.read().split("\n\n")
# Split the lines into calories per elf
elfs_char = [str.split(line, "\n") for line in src]
# Convert to integers
elfs_calories = [[int(calories) for calories in elf] for elf in elfs_char]
# Get the sums of calories by traversing the elf list
elfs = [*map(sum, elfs_calories)]
# ANSWER 1:
print(f"answer 1: {max(elfs)}")
# ANSWER 2:
# Sort the elfs, take the three biggest mofos
elfs.sort()
print(f"answer 2: {sum(elfs[-3:])}")