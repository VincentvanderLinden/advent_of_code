import numpy as np
from collections import deque

# Class to hold nodes
class Node:
    def __init__(self, coordinate):
        self.coordinate = coordinate
        self.dist = 0

    def __str__(self):
        return f"Node at: {self.coordinate}"

    def __eq__(self, other):
        return self.coordinate == other.coordinate


# Function to get valid neighbours
def get_neighbours(maze, node):
    maze_shape = np.shape(maze)
    coord = node.coordinate
    own_value = maze[node.coordinate]
    neighbour_coordinates = []
    neighbour_nodes = []

    if coord[0] > 0:
        up_value = maze[coord[0] - 1, coord[1]]
        if up_value <= own_value + 1.5:
            neighbour_coordinates.append((coord[0] - 1, coord[1]))
    if coord[0] < maze_shape[0] - 1:
        down_value = maze[coord[0] + 1, coord[1]]
        if down_value <= own_value + 1.5:
            neighbour_coordinates.append((coord[0] + 1, coord[1]))
    if coord[1] > 0:
        left_value = maze[coord[0], coord[1] - 1]
        if left_value <= own_value + 1.5:
            neighbour_coordinates.append((coord[0], coord[1] - 1))
    if coord[1] < maze_shape[1] - 1:
        right_value = maze[coord[0], coord[1] + 1]
        if right_value <= own_value + 1.5:
            neighbour_coordinates.append((coord[0], coord[1] + 1))

    for neighbour in neighbour_coordinates:
        neighbour_nodes.append(Node(coordinate=neighbour))
    return neighbour_nodes


# BFS algorithm
def traverse_maze(maze, start_node, end_node):
    # Initialize lists
    queue = deque()
    visited = set()
    # Add the starting node
    queue.append(start_node)

    # Go through the open_list
    while queue:
        # Pick the first node
        #print([x for x in queue])
        current_node = queue[0]
        # Pop the first value
        queue.popleft()
        # Add it to visited
        visited.add(current_node.coordinate)

        # If destination is found, be happy!
        if current_node == end_node:
            return current_node.dist
            break


        for neighbour in get_neighbours(maze, current_node):
           # print(neighbour)
            # Go through neighbours. If they are not yet visited, add them to the queue
            # And put them in visited with the correct distance
            neighbour.dist = current_node.dist + 1
            if neighbour.coordinate not in visited:
                queue.append(neighbour)
                visited.add(neighbour.coordinate)


with open('q12.in') as f:
    src = f.read().splitlines()

# Verbose way to interpret input, resulting in a np array with numbers
maze = []
for line in src:
    row = []
    for char in line:
        #using 26.5 to be able to go from y to E (as it is at elevation z, but i still want to recognize it)
        if char == 'S':
            char = 0.5
        elif char == 'E':
            char = 26.5
        else:
            char = ord(char) - 96
        row.append(char)
    maze.append(row)
maze = np.array(maze)

# Get the start and end coordinates
start = np.where(maze == 0.5)
end = np.where(maze == 26.5)
start_coord = [*zip(start[0], start[1])][0]
end_coord = [*zip(end[0], end[1])][0]

# # Add starting coordinate to open list
start_node = Node(coordinate=start_coord)
end_node = Node(coordinate=end_coord)

# # Go for it
answer1 = traverse_maze(maze, start_node, end_node)
print(f"Answer 1: {answer1}")


# part two: go backwards
# Get the start and end coordinates
# From 'a'
start = np.where(maze == 1)
# to 'E'
end = np.where(maze == 26.5)
start_coords = [*zip(start[0], start[1])]
end_coords = [*zip(end[0], end[1])][0]

end_node = Node(coordinate=end_coord)

answer2 = 10e9
for start_coord in start_coords: 
    # Add starting coordinate to open list
    start_node = Node(coordinate=start_coord)
    answer = traverse_maze(maze, start_node, end_node)
    if answer is not None:
        answer2 = min(answer, answer2)

print(f"Answer 2: {answer2}")


