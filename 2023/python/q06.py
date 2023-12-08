import re
with open ('q06.in') as f: 
    input = f.read().splitlines()

time, distance = map(lambda x: re.findall('\d+', x), input)

races = zip(map(int, time), map(int, distance))
p2_time = int(''.join(re.findall('\d+', input[0])))
p2_record = int(''.join(re.findall('\d+', input[1])))

# Part 1
total_wins = 0
for race in races: 
    time, record = race
    remaining_time = time
    winning = 0
    for speed in range(time): 
        distance_travelled = remaining_time * speed
        remaining_time -= 1
        if distance_travelled > record:
            winning += 1
    total_wins = winning if total_wins == 0 else total_wins * winning
print(total_wins)


# Part 2
winning = 0
remaining_time = p2_time
for speed in range(p2_time): 
        distance_travelled = remaining_time * speed
        remaining_time -= 1
        if distance_travelled > p2_record:
            winning += 1
print(winning)