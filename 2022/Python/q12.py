import numpy as np
from operator import attrgetter


class Node:
    def __init__(self, coordinate, parent):
        self.coordinate = coordinate
        self.parent = parent

        self.dist_to_previous = 0
        self.dist_to_end = 0
        self.cost = 0

    # def __str__(self):
    #     return f"\n----\nNode: {self.coordinate}\n" \
    #            f"scores are\n{self.dist_to_previous, self.dist_to_end, self.cost}\n" \
    #            f"parent_node: {self.parent}\n----"


# look around
def get_neighbours(maze, node):
    maze_shape = np.shape(maze)
    coord = node.coordinate
    print(f"node: {node}")
    print(f"node coordinate: {coord}")
    own_value = maze[node.coordinate]
    print(f"value: {own_value}")
    neighbour_coordinates = []
    neighbour_nodes = []

    if coord[0] > 0:
        up_value = maze[coord[0] - 1, coord[1]]
        if up_value <= own_value + 1:
            neighbour_coordinates.append((coord[0] - 1, coord[1]))
    if coord[0] < maze_shape[0]:
        down_value = maze[coord[0] + 1, coord[1]]
        if down_value <= own_value + 1:
            neighbour_coordinates.append((coord[0] + 1, coord[1]))
    if coord[1] > 0:
        left_value = maze[coord[0], coord[1] - 1]
        if left_value <= own_value + 1:
            neighbour_coordinates.append((coord[0], coord[1] - 1))
    if coord[1] < maze_shape[1]:
        right_value = maze[coord[0], coord[1] + 1]
        if right_value <= own_value + 1:
            neighbour_coordinates.append((coord[0], coord[1] + 1))
    print(neighbour_coordinates)
    for neighbour in neighbour_coordinates:
        neighbour_nodes.append(Node(coordinate=neighbour, parent=node))
    return neighbour_nodes


def traverse_maze(maze, start_node, end_node):
    # Initialize lists
    open_list = []
    closed_list = []

    open_list.append(start_node)
    # Sort the open list by cost
    while len(open_list) > 0:
        # Take first item from open_list
        current_node = open_list[0]
        print(f" x : {open_list} , {open_list[0]}, {current_node.coordinate}")
        current_idx = 0
        # If there are items with a lower cost, pick that one
        for idx, item in enumerate(open_list):
            if item.cost < current_node.cost:
                current_node = item
                current_idx = idx
        print(current_node.coordinate)
        # Pop it from the open_list
        open_list.pop(current_idx)
        # Move it to the closed_list
        closed_list.append(current_node)

        if current_node == end_node:
            print('hurrah')
            return

        # Find its neighbours
        print(f"current_node: {current_node}, {current_node.coordinate}")
        neighbour_nodes = get_neighbours(maze, current_node)
        print(f"neighbour_nodes:  {neighbour_nodes}")
        for neighbour in neighbour_nodes:
            for closed_node in closed_list:
                if neighbour == closed_node:
                    continue
            # dist_to_previous (G)
            dist_to_previous = current_node.dist_to_previous + 1
            # dist_to_end (H) Manhattan
            dist_to_end = abs(neighbour.coordinate[0] - end_node.coordinate[0]) + \
                          abs(neighbour.coordinate[1] - end_node.coordinate[1])
            # node_cost (F)
            cost = dist_to_previous + dist_to_end

            child_node = Node(coordinate=neighbour,
                              parent=current_node)
            child_node.dist_to_previous = dist_to_previous
            child_node.dist_to_end = dist_to_end
            child_node.cost = cost

            for open_node in open_list:
                if child_node.coordinate == open_node.coordinate and \
                        child_node.dist_to_previous > open_node.dist_to_previous:
                    continue
            open_list.append(child_node)



# A*
with open('q12.in') as f:
    input = f.read().splitlines()

# Verbose way to interpret input, resulting in a np array with numbers
maze = []
for line in input:
    row = []
    for char in line:
        if char == 'S':
            char = 0
        elif char == 'E':
            char = 27
        else:
            char = ord(char) - 96
        row.append(char)
    maze.append(row)
maze = np.array(maze)

start = np.where(maze == 0)
end = np.where(maze == 27)
start_coord = [*zip(start[0], start[1])][0]
end_coord = [*zip(end[0], end[1])][0]
# Look around

# Add starting coordinate to open list
start_node = Node(start_coord, None)
end_node = Node(end_coord, None)

traverse_maze(maze, start_node, end_node)
