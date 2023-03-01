with open('q13.in') as f:
    input = f.read().split('\n\n')
    input = [line.split('\n') for line in input]

for line in input[:2]:
    left = eval(line[0])
    right = eval(line[1])
    for char in left: 
        if type(char) is int: 
            print('ads')