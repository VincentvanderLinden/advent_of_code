import re
from math import prod
with open('q02.in') as f: 
    games = f.read().splitlines()

answer1 = 0
answer2 = 0

for game in games:
    game_id = int(re.findall(r'\d+', game)[0])
    gems = re.findall(r'(\d+) (blue|red|green)', game)
    possible_game = True
    gem_dict = {'green': 0, 'red': 0, 'blue': 0}
    for gem in gems: 
        n, c = int(gem[0]), gem[1]
        if (c == 'red' and n > 12) or \
            (c == 'green' and n > 13) or \
             (c == 'blue' and n > 14): 
            possible_game = False
        
        if n > gem_dict[c]: 
            gem_dict[c] = n

    if possible_game: 
        answer1 += game_id

    answer2 += prod(gem_dict.values())

print(f"Answer 1: {answer1}")
print(f"Answer 2: {answer2}")