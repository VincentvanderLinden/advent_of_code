import numpy as np
with open('q07.in') as f:
    positions = np.array([*map(int, f.read().split(','))])

# Initialize with loads of fuel
least_fuel = 1e9

# Loop through all crabs
for crab in range(len(positions)):
    # Determine total fuel cost by substracting crab from np array
    fuel = sum(abs(positions - crab))
    # If the fuel cost is lower than it already was, put that in least_full
    if fuel < least_fuel:
        least_fuel = fuel

print(f"Answer 1: {least_fuel}")

# Part two 
least_fuel = 1e9

# Triangular number formula for 1+2+3+..+n
def triangular(n): 
    return (n*(n+1))/2

for crab in range(len(positions)):
    # Determine total fuel cost by substracting crab from np array
    fuel = sum(triangular(abs(positions - crab)))
    # If the fuel cost is lower than it already was, put that in least_full
    if fuel < least_fuel:
        least_fuel = fuel

print(f"Answer 2: {int(least_fuel)}")