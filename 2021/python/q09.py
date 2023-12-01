import math
with open('q09.in') as f: 
    src = f.read().split('\n')
# Create Matrix
cave = [[int(tile) for tile in row] for row in src]

# Initialize list for lowest coordinates
lowest_coords = []

# Generate dict of coordinates
coords = {}
for row in range(len(cave)): 
    for col in range(len(cave[0])):
        coords[(row, col)] = cave[row][col]

# Use dict to look around each coordinate

for row in range(len(cave)): 
    for col in range(len(cave[0])):
        # Look around using .get to avoid keyerrors, using inf if it's on edge of matrix
        up = coords.get((row - 1, col), float('inf'))
        down = coords.get((row + 1, col), float('inf'))
        left = coords.get((row, col - 1), float('inf'))
        right = coords.get((row, col + 1), float('inf'))
        if cave[row][col] < min(up, down, left, right): 
            lowest_coords.append((row, col))

print(f"Answer 1: {sum([coords[coord] + 1 for coord in lowest_coords])}")



def get_adjacent_coords(coord_dict, coordinate_list, adjacent_coords):
    # Go through the coordinates (copy because it's a list)
    for coords in coordinate_list.copy(): 
        # Check if coordinates are found at all
        found_coordinates = 0
        # Add own coordinate to the set of coordinates
        adjacent_coords.add((coords[0], coords[1]))
        
        # Generate up coordinate, check if it's a valid key, not 9 and not already visited
        up = (coords[0] - 1, coords[1]) 
        if up in coord_dict.keys() and coord_dict[up] != 9 and up not in adjacent_coords: 
            adjacent_coords.add(up)
            found_coordinates += 1
        # Generate down coordinate, check if it's a valid key, not 9 and not already visited
        down = (coords[0] + 1, coords[1])
        if down in coord_dict.keys() and coord_dict[down] != 9 and down not in adjacent_coords: 
            adjacent_coords.add(down)
            found_coordinates += 1
        # Generate left coordinate, check if it's a valid key, not 9 and not already visited
        left = (coords[0], coords[1] - 1)
        if left in coord_dict.keys() and coord_dict[left] != 9 and left not in adjacent_coords: 
            adjacent_coords.add(left)
            found_coordinates += 1
        # Generate right coordinate, check if it's a valid key, not 9 and not already visited
        right = (coords[0], coords[1] + 1)
        if right in coord_dict.keys() and coord_dict[right] != 9 and right not in adjacent_coords: 
            adjacent_coords.add(right)
            found_coordinates += 1
        
        #If no coordinates are found, the wall has been hit. Return that set
        if found_coordinates == 0:
            continue
        # If new coordinates are found, there might be even more Mike! Recurse!
        else: 
            adjacent_coords.update(get_adjacent_coords(coord_dict, adjacent_coords, adjacent_coords))
    return adjacent_coords
    

basins = []
for row in range(len(cave)): 
    for col in range(len(cave[0])):
        # Inititate empty set
        adjacent_coords = set()
        if (not any((row, col) in x for x in basins)) and coords[(row, col)] != 9: 
           basins.append(get_adjacent_coords(coords, [(row, col)], adjacent_coords))

# Multiply the three largest lists
print(f"Answer 2: {math.prod(sorted([len(x) for x in basins if len(x) != 0])[-3:])}")

