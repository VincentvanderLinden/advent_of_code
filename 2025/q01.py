with open('q01.in') as f: 
    input = f.read().splitlines()
    
pos = 50
answer1 = 0

for line in input: 
    dir = line[0]
    n = int(line[1:])

    s = n if dir == 'R' else -n

    pos = (pos + s) % 100    

    if pos == 0: 
        answer1 += 1
    
print(f"Answer 1: {answer1}")

with open('q01.in') as f: 
    input = f.read().splitlines()

answer2 = 0
pos = 50

for line in input: 
    dir = line[0]
    n = int(line[1:])
    
    if dir == 'L':
            answer2 += ((100-pos)%100 + n)//100
            n *= -1
    else:
        answer2 += (pos+n)//100
    pos = (pos+n)%100
    
print(f"Answer 2: {answer2}")