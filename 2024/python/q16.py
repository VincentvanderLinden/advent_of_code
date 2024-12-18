import heapq

# Define the maze
with open('q16.in') as f:
    maze = [list(line) for line in f.read().splitlines()]
    
# Directions: (dx, dy, cost)
directions = {
    'E': (0, 1, 1),
    'W': (0, -1, 1),
    'N': (-1, 0, 1),
    'S': (1, 0, 1)
}

# Rotation cost
rotation_cost = 1000

# Find the start and end positions
start = None
end = None
for i in range(len(maze)):
    for j in range(len(maze[i])):
        if maze[i][j] == 'S':
            start = (i, j)
        elif maze[i][j] == 'E':
            end = (i, j)

def dijkstra(start, end):
    pq = [(0, start[0], start[1], 'E', [])]  # (score, x, y, direction, path)
    visited = set()
    
    while pq:
        score, x, y, direction, path = heapq.heappop(pq)
        
        if (x, y) == end:
            return score, path
        
        if (x, y, direction) in visited:
            continue
        
        visited.add((x, y, direction))
        
        # Move forward
        dx, dy, move_cost = directions[direction]
        nx, ny = x + dx, y + dy
        if maze[nx][ny] != '#':
            heapq.heappush(pq, (score + move_cost, nx, ny, direction, path + [(nx, ny, direction)]))
        
        # Rotate 90
        new_direction = {'E': 'S', 'S': 'W', 'W': 'N', 'N': 'E'}[direction]
        heapq.heappush(pq, (score + rotation_cost, x, y, new_direction, path + [(x, y, new_direction)]))
        
        # Rotate rotate -90
        new_direction = {'E': 'N', 'N': 'W', 'W': 'S', 'S': 'E'}[direction]
        heapq.heappush(pq, (score + rotation_cost, x, y, new_direction, path + [(x, y, new_direction)]))

min_score, path = dijkstra(start, end)

print(f"Answer 1: {min_score}.")