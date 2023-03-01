import re
import numpy as np

with open('q04.in') as f:
    src = f.read().split('\n\n')
src_parsed = [line.split('\n') for line in src]
numbers = [*map(int, re.findall(r"\d+", *src_parsed[0]))]
boards = src_parsed[1:]

# List to store bingo results per board
bingo_results = []

for board_idx, board in enumerate(boards): 
    # Create empty arrays
    board_ar = np.zeros((5, 5))
    marked_ar = np.zeros((5, 5))
    # Add numbers to board
    for idx, line in enumerate(board): 
        board_ar[idx] = ([*map(int, re.findall(r"\d+", line))])
    # Draw number
    for number_idx, number in enumerate(numbers): 
        # Mark the number on the board
        marked_ar[np.where(board_ar == number)] = 1
        # Check if a row or column has a sum of 5
        if any(np.sum(marked_ar, axis=0) == 5) or any(np.sum(marked_ar, axis=1) == 5):
            # Add result to the bingo_results
            bingo_results.append([board_idx, number_idx, number, np.sum(board_ar[marked_ar == 0])])
            # Get outta here!
            break

# Best board has lowerst amount of rounds (number_idx)
best_board = min(bingo_results, key=lambda x: x[1])

print(f"Answer 1:{int(best_board[2]*best_board[3])}")

# Best board has lowerst amount of rounds (number_idx)
worst_board = max(bingo_results, key=lambda x: x[1])

print(f"Answer 2:{int(worst_board[2]*worst_board[3])}")