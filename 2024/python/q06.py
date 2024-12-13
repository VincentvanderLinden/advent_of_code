import numpy as np

with open('q06.in') as f: 
    inp = f.readlines()
    
maze_input = np.array([list(i.strip()) for i in inp])

class Maze: 
    def __init__(self, maze: list, name: str): 
        self.maze = maze
        self.name = name
        self.starting_position = self.find_starting_position(self.maze)
                    
    def __repr__(self) -> str: 
        new_line = '\n    '
        return f" {self.name} \n    {new_line.join(''.join(row) for row in self.maze)}\n"
        
    def __getitem__(self, row) -> list:
        return self.maze[row]
      
    def __len__(self): 
        return len(self.maze)
        
    def find_starting_position(self, maze: list) -> np.array: 
        for row in range(len(maze)): 
            for col in range(len(maze[0])):
                if maze[row][col] == '^': 
                    coords = np.array((row, col))
                    return coords
        
class Guard: 
    """
    The guard class. 
     
    Methods: 
    """
    def __init__(self, name: str): 
        self.name = name
        self.directions = {
            'up':       {'move': (-1, 0), 'icon': '^', 'next_dir': 'right'}, 
            'right':    {'move': (0, 1) , 'icon': '>', 'next_dir': 'down'}, 
            'down':     {'move': (1, 0) , 'icon': 'v', 'next_dir': 'left'}, 
            'left':     {'move': (0, -1), 'icon': '<', 'next_dir': 'up'}
        }
        
        self.maze = None
        self.position = None
        self.in_the_maze = False
        self.current_direction = 'up'
        
    def __repr__(self): 
        if self.position is None: 
            pos = 'outside the maze'
        else: 
            pos = 'at coordinates ' + str(self.position)
        return f"{self.name} is {pos}, looking {self.current_direction}."
      
    # Method to enter a maze    
    def enter_maze(self, maze: list): 
        # Set relevant attributes
        self.maze = maze
        if self.maze.starting_position is None: 
            raise ValueError('The given maze does not have a starting position!')
        else: 
            self.position = self.maze.starting_position
        self.in_the_maze = True
        row, col = self.position
        self.coordinates_touched = set() 
        self.coordinates_touched.add(tuple(self.position))
        self.obstacles_hit = set()
        self.stuck_in_loop = False
        self.new_obstacle_row = 0
        self.new_obstacle_col = 0
        
    # Check if there is an obstacle coming up
    def obstacle_found(self, direction: str): 
        next_row, next_col = self.position + self.directions[direction].get('move')
        if (next_row, next_col, self.current_direction) in self.obstacles_hit: 
            self.stuck_in_loop = True
        self.obstacles_hit.add((next_row, next_col, self.current_direction))
        return True if self.maze[next_row][next_col] == '#' else False
    
    # Check if the guard found the exit   
    def exit_found(self, direction:str): 
        next_row, next_col = self.position + self.directions[direction].get('move')
        return True if next_row < 0 or next_row >= len(self.maze) or \
                       next_col < 0 or next_col >= len(self.maze[0]) else False
           
            
    def move(self, direction: str): 
        """
        Moves the guard in a given direction, 
        checking for obstacles and the exit. 
        """
        
        # Keep track of the old position
        old_row, old_col = self.position 
        
        if self.stuck_in_loop: 
            self.in_the_maze = False
            
        # Run away if exit is found
        if self.exit_found(self.current_direction): 
            self.in_the_maze = False
        
        
            
        # Change direction is obstacle found
        elif self.obstacle_found(self.current_direction): 
            self.current_direction = self.directions[self.current_direction].get('next_dir')
        
            
        # Actual guard move
        else:  
            # Check the directions dictionary to see which way to move (add coordinates)
            # And move the guard
            self.position += self.directions[self.current_direction].get('move')
            # Determine new position and store it in the coordinates_touched
            new_row, new_col = self.position
            self.coordinates_touched.add(tuple(self.position))
            
            # Modify the maze for printing purposes
            # self.maze[old_row][old_col] = 'X'
            # self.maze[new_row][new_col] = self.directions[self.current_direction].get('icon')
            
    # Auto walk through the maze
    def clear_maze(self): 
        while self.in_the_maze: 
            self.move(self.current_direction)
      
    # Count the moves made      
    def count_moves(self): 
        return len(self.coordinates_touched)
            
            
    
maze = Maze(maze_input, 'THE MAZE OF DOOM')  
bob = Guard(name='Bob')
bob.enter_maze(maze)
bob.clear_maze()

print(f"Question 1: {bob.count_moves()}", flush=True)

res = 0
for i in range(len(maze_input)): 
    for j in range(len(maze_input[0])): 
        new_maze = maze_input.copy()
        if new_maze[i][j] == '.': 
            new_maze[i][j] = '#'  
        maze = Maze(new_maze, name='The Maze')
        bob = Guard(name='Bob')
        bob.enter_maze(maze)
        bob.clear_maze()
        res+=bob.stuck_in_loop
        print(i, j, res, flush=True)

print(f"Question 2: {res}")
