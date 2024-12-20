import time
import numpy as np
from collections import deque

def timeit(f):

    def timed(*args, **kw):

        ts = time.time()
        result = f(*args, **kw)
        te = time.time()

        print(f"I timed your badly written function: '\033[35m{f.__name__}\033[0m'. It took: \033[36m{te-ts:2.2f} seconds\033[0m to run... You absolute \033[91mnoob...\033[0m")
        return result

    return timed


def read_matrix_from_file(filename: str, to_numpy: bool = False, to_int: bool = False): 
    with open(filename, 'r') as f: 
        if to_int: 
            inp = [list(map(int, i.strip())) for i in f.readlines()]
 
        else: 
            inp = [list(i.strip()) for i in f.readlines()]
            
        if to_numpy: 
            inp = np.array(inp)
    return inp

class FancyMatrix: 
    def __init__(self, maze_input: list[list]): 
        self.maze = maze_input
        self.HEIGHT = len(self.maze)
        self.WIDTH = len(self.maze[0])
    
    def __repr__(self): 
        new_line = '\n'
        return f"{new_line.join(''.join(row) for row in self.maze)}"
        
    def __getitem__(self, row) -> list:
        return self.maze[row]
      
    def __len__(self): 
        return len(self.maze)
    
    def __copy__(self):
        return type(self)(self.maze)
    
    
    
    def find_value(self, val: str, exclude_walls: int = False) -> tuple:
        res = []
        height_range = range(len(self.maze))
        width_range = range(len(self.maze[0]))
        if exclude_walls: 
            height_range = range(1, len(self.maze)-1)
            width_range = range(1, len(self.maze[0])-1)
            
        for row in height_range:
            for col in width_range: 
                if self.maze[row][col] == val:
                    res.append((row, col))
        if len(res) == 0: 
            return None
        elif len(res) == 1: 
            return res[0]
        return res
                
                
                
    def is_valid_move(self, visited: set, r: int , c: int, invalid_chars: list= ['#']) -> list: 
        
        if (0 <= r < len(self.maze) 
            and 0 <= c < len(self.maze[0]) 
            and self.maze[r][c] not in invalid_chars
            and (r, c) not in visited
        ):
            return True
        return False
    
    """BFS"""
    def bfs(self, start: tuple, end: tuple) -> dict:
        visited = set()
        queue = deque([(start, 0)])
        visited.add(start)

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        while queue: 
            (r, c), length = queue.popleft()
            
            if (r, c) == end: 
                return {"path": visited, "length": length}

            for d in directions: 
                n_r, n_c = r + d[0], c + d[1]
                if self.is_valid_move(visited, n_r, n_c): 
                    queue.append(((n_r, n_c), length+1))
                    visited.add((n_r, n_c))
                
                    
        return {"path": None, "length": None}