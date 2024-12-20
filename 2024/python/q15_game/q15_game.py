import pygame
import sys

# Initialize Pygame
pygame.init()

# Define constants
TILE_SIZE = 100
MAZE = [
    "##########",
    "#..O..O.O#",
    "#......O.#",
    "#.OO..O.O#",
    "#..O@..O.#",
    "#O#..O...#",
    "#O..O..O.#",
    "#.OO.O.OO#",
    "#....O...#",
    "##########"
]
WIDTH = len(MAZE[0]) * TILE_SIZE
HEIGHT = len(MAZE) * TILE_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("HO HO HO")

# Load images
robot_img = pygame.image.load('pepe.png')
robot_img = pygame.transform.scale(robot_img, (TILE_SIZE, TILE_SIZE))
box_img = pygame.image.load('box.png')
box_img = pygame.transform.scale(box_img, (TILE_SIZE, TILE_SIZE))
wall_img = pygame.image.load('tree.png')
wall_img = pygame.transform.scale(wall_img, (TILE_SIZE, TILE_SIZE))

empty_img = pygame.Surface((TILE_SIZE, TILE_SIZE))
empty_img.fill(BLACK)


# Find the robot's initial position
robot_pos = None
for y, row in enumerate(MAZE):
    for x, tile in enumerate(row):
        if tile == '@':
            robot_pos = (x, y)
            break
    if robot_pos:
        break

def is_within_bounds(pos):
    return 0 <= pos[0] < len(MAZE[0]) and 0 <= pos[1] < len(MAZE)

def is_empty_or_box(pos):
    return MAZE[pos[1]][pos[0]] in ('.', 'O')

def move_robot(new_pos):
    global robot_pos
    if is_within_bounds(new_pos):
        if MAZE[new_pos[1]][new_pos[0]] == '.':
            robot_pos = new_pos
        elif MAZE[new_pos[1]][new_pos[0]] == 'O':
            # Check if we can push all boxes in the direction of movement
            direction = (new_pos[0] - robot_pos[0], new_pos[1] - robot_pos[1])
            current_pos = new_pos
            boxes_to_move = []
            while is_within_bounds(current_pos) and MAZE[current_pos[1]][current_pos[0]] == 'O':
                boxes_to_move.append(current_pos)
                current_pos = (current_pos[0] + direction[0], current_pos[1] + direction[1])
            if is_within_bounds(current_pos) and MAZE[current_pos[1]][current_pos[0]] == '.':
                # Move all boxes
                for box in reversed(boxes_to_move):
                    MAZE[box[1]] = MAZE[box[1]][:box[0]] + '.' + MAZE[box[1]][box[0]+1:]
                    new_box_pos = (box[0] + direction[0], box[1] + direction[1])
                    MAZE[new_box_pos[1]] = MAZE[new_box_pos[1]][:new_box_pos[0]] + 'O' + MAZE[new_box_pos[1]][new_box_pos[0]+1:]
                robot_pos = new_pos

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            new_pos = list(robot_pos)
            if event.key == pygame.K_UP:
                new_pos[1] -= 1
            elif event.key == pygame.K_DOWN:
                new_pos[1] += 1
            elif event.key == pygame.K_LEFT:
                new_pos[0] -= 1
            elif event.key == pygame.K_RIGHT:
                new_pos[0] += 1

            move_robot(tuple(new_pos))

    # Draw the maze
    for y, row in enumerate(MAZE):
        for x, tile in enumerate(row):
            if tile == '#':
                screen.blit(wall_img, (x * TILE_SIZE, y * TILE_SIZE))
            elif tile == 'O':
                screen.blit(box_img, (x * TILE_SIZE, y * TILE_SIZE))
            elif tile == '.':
                screen.blit(empty_img, (x * TILE_SIZE, y * TILE_SIZE))
            elif tile == '@':
                screen.blit(empty_img, (x * TILE_SIZE, y * TILE_SIZE))

    # Draw the robot
    screen.blit(robot_img, (robot_pos[0] * TILE_SIZE, robot_pos[1] * TILE_SIZE))

    pygame.display.flip()

pygame.quit()
sys.exit()