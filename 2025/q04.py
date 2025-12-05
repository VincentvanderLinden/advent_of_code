from utils import read_matrix_from_file, FancyMatrix


maze_list = read_matrix_from_file(filename='q04.in')
m = FancyMatrix(maze_input=maze_list)

# N, NE, E, SE, S, SW, W, NW
DIRS = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]

def has_less_than_x_neighbours(maze: list[list], 
                               coordinate: tuple, 
                               x: int=4, 
                               character: str='@', 
                               directions: list=DIRS) -> bool:
    neighbours = 0
    
    for dir in directions: 
        look_at_row, look_at_col = coordinate[0]+dir[0], coordinate[1]+dir[1]
        if 0<=look_at_row<maze.HEIGHT and 0<=look_at_col<maze.WIDTH: 
            if maze[look_at_row][look_at_col] == character: 
                neighbours += 1

    return True if neighbours < x else False


# Part 1
answer1 = 0

for r in range(m.HEIGHT): 
    for c in range(m.WIDTH):
        
        if m[r][c] != '@': 
            pass
        else:
            answer1 += has_less_than_x_neighbours(maze=m, coordinate=(r,c), x=4) 

print(f"Answer1: {answer1}")

# Part 2
answer2 = 0
paper_can_be_removed = True

while paper_can_be_removed: 
    paper_to_remove = []
    for r in range(m.HEIGHT): 
        for c in range(m.WIDTH):

            if m[r][c] != '@': 
                pass
            else: 
                if has_less_than_x_neighbours(maze=m, coordinate=(r,c), x=4): 
                    answer2 += 1
                    paper_to_remove.append((r, c))
    
    # All paper stuck, stop working
    if len(paper_to_remove) == 0:
        paper_can_be_removed = False 
    
    # Update maze    
    for coord in paper_to_remove: 
        m[coord[0]][coord[1]] = '.'          

print(f"Answer2: {answer2}")

