import re

with open('q02.in') as f: 
    input = f.read().split(',')
    
answer1 = 0
answer2 = 0

for line in input: 
    a, b = map(int, line.split('-'))
    for i in range(a, b+1): 
        j = str(i)
        if j[:len(j)//2] == j[len(j)//2:]: 
            answer1 += i
            
        # Part 2
        match = re.match(r"^([0-9]+?)\1+$", j)
        if  match: 
            answer2 += i
            # print(i, match.groups(), match.span())
            next

print(f"Answer 1: {answer1}")
print(f"Answer 2: {answer2}")


