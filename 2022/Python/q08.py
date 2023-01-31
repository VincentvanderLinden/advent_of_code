import numpy as np

with open('q08.in') as file:
    input = file.read().splitlines()
# Create lines of trees and turn into ndarray for fun
forest_input = np.array([[int(tree) for tree in row] for row in input])


# Calculate scenic scores
def calculate_scenic_score(direction, tree_height, list_of_trees):
    # For Up and Left: Reverse the list of trees so you are looking the right way :)
    if direction in ['left', 'up']:
        list_of_trees = [*reversed(list_of_trees)]
    # If all trees are shorter, just return the number of trees
    if max(list_of_trees) < tree_height:
        scenic_score = len(list_of_trees)
    # Otherwise, count how many trees there are until you reach a three of equal or greater height
    else:
        scenic_score = next(idx for idx, value in enumerate(list_of_trees) if value >= tree_height) + 1
    return scenic_score


def check_trees(forest, row, col):
    tree_height = forest[row, col]
    # Check if tree is on the edge, these are always visible
    if any([row in [0, forest.shape[0]-1], col in [0, forest.shape[1]-1]]):
        return {'visible': True, 'scenic_score': 0}
    else:
        # Get the lists of trees in all directions
        trees_up = forest[:row, col]
        trees_down = forest[row + 1:, col]
        trees_left = forest[row, :col]
        trees_right = forest[row, col + 1:]
        # Calculate scenic scores
        scs_u = calculate_scenic_score('up', tree_height, trees_up)
        scs_d = calculate_scenic_score('down', tree_height, trees_down)
        scs_l = calculate_scenic_score('left', tree_height, trees_left)
        scs_r = calculate_scenic_score('right', tree_height, trees_right)
        scenic_score = scs_u * scs_d * scs_l * scs_r

        # If all directions have trees of equal or greater height, return visible: False (invisible)
        if min([max(trees_up), max(trees_down), max(trees_left), max(trees_right)]) >= tree_height:
            return {'visible': False, 'scenic_score': scenic_score}
        # Otherwise, it's the highest tree and therefore visible, return visible: True
        else:
            return {'visible': True, 'scenic_score': scenic_score}


# Initialize Answers
visible_trees = 0
max_scenic_score = 0
# Check every tree's visibility and add 1 to visible_trees
for row in range(forest_input.shape[0]):
    for col in range(forest_input.shape[1]):
        tree_check = check_trees(forest=forest_input, row=row, col=col)
        # Check visibility and add True (1) of False (0) to the visible_trees
        visible_trees += tree_check['visible']
        # Check scenic_score and change it to a new scenic_score if it is higher
        # than the previous scenic_score
        max_scenic_score = max(max_scenic_score, tree_check['scenic_score'])

print(f"answer 1: {visible_trees}")
print(f"answer 2: {max_scenic_score}")
