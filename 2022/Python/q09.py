import re

with open('q09.in') as file:
    input = file.read().splitlines()


# Head moving function
def move_head(x, y, direction):
    # Determine modifier. (Down and left need to subtract from the coordinates
    if direction in ['D', 'L']:
        modifier = -1
    else:
        modifier = 1
    # Add 1 to head coordinates using the modifier, dependent on direction
    if direction in ['U', 'D']:
        y = y + (1 * modifier)
    elif direction in ['L', 'R']:
        x = x + (1 * modifier)
    return x, y


def move_tail(x, y, head_x, head_y):
    # Tail will only move if either x or y of the head are 2 away
    if any([abs(head_x - x) > 1, abs(head_y - y) > 1]):
        # Handle nasty diagonal moves (manhattan distance is higher than 2):
        if abs(head_x - x) + abs(head_y - y) > 2:
            # If it is 2 away on the x-axis, it will snap to the same y-axis as the head
            # Nasty case where previous tail went 2x2 away due to rope behavior
            if (abs(head_x - x) == 2) and (abs(head_y - y) == 2):
                x = int(x + (x - head_x) / 2)
                y = int(y + (y - head_y) / 2)
            elif abs(head_x - x) == 2:
                y = head_y
            # If it is 2 away on the y-axis, it will snap to the same x-axis as the head
            elif abs(head_y - y) == 2:
                x = head_x
        # Do regular movements
        if head_x - x > 0:
            x = head_x - 1
        if head_x - x < 0:
            x = head_x + 1
        if head_y - y > 0:
            y = head_y - 1
        if head_y - y < 0:
            y = head_y + 1
    return x, y


# Set initial coordinates
head_x, head_y, tail_x, tail_y = 0, 0, 0, 0
# Create set for tail positions
tail_visits = set()

for instruction in input:
    direction, amount = instruction[0], int(re.findall(r"\d+", instruction)[0])
    for _ in range(amount):
        # Move the head
        head_x, head_y = move_head(head_x, head_y, direction)
        # Move the tail using the head coordinates
        tail_x, tail_y = move_tail(tail_x, tail_y, head_x, head_y)
        # Put the tail position in the tail_position set
        tail_visits.add((tail_x, tail_y))

print(f"Answer 1: Tail visited {len(tail_visits)} positions")

# Part 2
# Set initial coordinates
head_x, head_y = 0, 0
# Create nine tail positions
tail_positions = [(0, 0) for _ in range(9)]
# Create set for tail positions
tail_visits = set()

for instruction in input:
    direction, amount = instruction[0], int(re.findall(r"\d+", instruction)[0])
    for _ in range(amount):
        # Move the head
        head_x, head_y = move_head(head_x, head_y, direction)

        # Move the other 8 tails using the tail coordinates
        for idx, tail in enumerate(tail_positions):
            # First tail follows head
            if idx == 0:
                tail_positions[idx] = move_tail(tail[0], tail[1], head_x, head_y)
            else:
                tail_positions[idx] = move_tail(tail[0], tail[1],
                                                tail_positions[idx - 1][0], tail_positions[idx - 1][1])

            # Store the last tail's position
            if idx == 8:
                tail_visits.add((tail_positions[idx][0], tail_positions[idx][1]))

print(f"Answer 2: Tail visited {len(tail_visits)} positions")
