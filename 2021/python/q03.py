import numpy as np
with open('q03.in') as f:
    src = f.read().splitlines()

# Turn src into np array
diagnostic = np.array([[*line] for line in src])

# Create gamma and epsilon as empty strings
gamma = ''
epsilon = ''
# For all columns
for col in range(np.shape(diagnostic)[1]):
    # Get the counts per value for each column
    values, counts = np.unique(diagnostic[:, col], return_counts=True)
    # Concatenate the most occuring one to gamma
    gamma += values[counts.argmax()]
    # Concatenate the least occuring one to gamma
    epsilon += values[counts.argmin()]

# Translate the gamma and epsilon values
print(f"Answer 1: {int(gamma, 2) * int(epsilon, 2)}")


# Part 2: 

# For all columns

def calc_oxygen(ar, col):
        # Return if the array has one entry
        if len(ar) == 1:
            return ar
        # Get the counts per value for each column
        values, counts = np.unique(ar[:, col], return_counts=True)
        # If there are equal amount of ones and zeros
        if len(np.unique(counts)) == 1:
            most_common_bit = '1'
        else: 
             # Concatenate the most occuring one to gamma
            most_common_bit = values[counts.argmax()]
        oxygen_array = ar[ar[:,col] == most_common_bit]
        return calc_oxygen(oxygen_array, col + 1)

def calc_carbon(ar, col):
        # Return if the array has one entry
        if len(ar) == 1:
            return ar
        # Get the counts per value for each column
        values, counts = np.unique(ar[:, col], return_counts=True)
        # If there are equal amount of ones and zeros
        if len(np.unique(counts)) == 1:
            least_common_bit = '0'
        else: 
            # Concatenate the most occuring one to gamma
            least_common_bit = values[counts.argmin()]
        carbon_array = ar[ar[:,col] == least_common_bit]
        return calc_carbon(carbon_array, col + 1)

print(f"Answer 2: {int(''.join(*calc_oxygen(diagnostic, 0)), 2) * int(''.join(*calc_carbon(diagnostic, 0)), 2)}")


