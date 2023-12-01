with open('q01.in') as f: 
    # Read lines as integers
    src = [*map(int, f.read().splitlines())]

# Initiate number_of_increases
number_of_increases = 0

# Loop through 
for idx, value in enumerate(src):
    # Skip index 0
    if idx == 0:
        continue
    # Add to number_of_increases if current value is larger than previous value
    if value > src[idx - 1]: 
        number_of_increases += 1

# Print answer
print(f"Answer 1 : {number_of_increases}")

number_of_increases = 0

# Loop through 
for idx, value in enumerate(src):
    # Skip index 0
    if idx == 0:
        continue
    # Compare sum of three values from index to sum of three values from idx - 1
    if sum(src[idx:idx+3]) > sum(src[idx-1:idx+2]): 
        number_of_increases += 1

print(f"Answer 2 : {number_of_increases}")