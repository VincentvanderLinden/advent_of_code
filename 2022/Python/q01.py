#Open file and split on double returns
with open('q01.in') as f:
    input = f.read().split("\n\n")
#Split the lines into calories per elf
input = [str.split(line, "\n") for line in input]
#Convert to integers
input = [[int(calories) for calories in elf] for elf in input]
#Get the sums of calories by traversing the elf list
elfs = [*map(sum, input)]
#ANSWER 1: 
print(f"answer 1: {max(elfs)}")
#ANSWER 2:
elfs.sort()
print(f"answer 2: {sum(elfs[-3:])}")