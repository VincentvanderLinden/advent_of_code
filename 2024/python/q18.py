from collections import deque
import utils

SIZE = 71
maze = []

for r in range(SIZE): 
    maze.append(['.']*SIZE)

with open('q18.in') as f: 
    for line in f.read().splitlines()[:1024]:
        c,r = map(int, line.split(',') )    
        maze[r][c] = '#'

start = (0, 0)
end = (SIZE-1, SIZE-1)

maze = utils.FancyMatrix(maze)
bfs = maze.bfs(start, end)['length']

print(f"Answer 1: {bfs}")



with open('q18.in') as f: 
    for line in f.read().splitlines()[1024:]:
        c,r = map(int, line.split(',') )    
        maze[r][c] = '#'
        if maze.bfs(start, end)['length'] is None: 
            print(f"Answer 2: {c},{r}")
            break
        
