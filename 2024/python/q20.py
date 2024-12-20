import utils
from collections import Counter
import sys 
from copy import copy

sys.setrecursionlimit(2000)

m = utils.read_matrix_from_file(filename='q20.in')


maze = utils.FancyMatrix(m)
start = maze.find_value('S')
end = maze.find_value('E')

l = maze.bfs(start=start, end=end)['length']



removed = []
lengths = dict()
original_length = maze.bfs(start, end)['length']
walls = maze.find_value('#', exclude_walls=True)

@utils.timeit
def part1():
    res = 0
    for ix, wall in enumerate(walls): 
        if ix == 0: 
            pass
        else: 
            maze[walls[ix-1][0]][walls[ix-1][1]] = '#'

        maze[wall[0]][wall[1]] = '.'
        
        l = original_length - maze.bfs(start, end)['length']
        if l >= 100: 
            res += 1
    return res

res = part1()
print(f"Answer 1: {res}")   

