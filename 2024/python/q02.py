with open('q02.in') as f: 
    inp = f.read().splitlines()
    lines = list(map(str.split, inp))

    
def check_line (line: list) -> bool: 
    valid = True
    digits = list(map(int, line))

    if digits[1] == digits[0]: 
        valid = False
    order = 1 if digits[1] > digits[0] else -1
    if order == -1: 
        for ix, d in enumerate(digits[1:]): 
            if not 1 <= digits[ix] - d <= 3: 
                valid = False
                continue
    elif order == 1:        
        for ix, d in enumerate(digits[1:]): 
            if not 1 <= d - digits[ix] <= 3: 
                valid = False
                continue
    return valid
    
res = 0

for line in lines: 
    res += check_line(line)
    
print(f"Question 1: {res}")

res = 0

for line in lines: 
    super_valid = check_line(line)
    if super_valid: 
        res+=1
    else: 
        for i in range(len(line)): 
            new_line = line[:i] + line[i+1:]
            if check_line(new_line): 
                res+=1
                break
            
print(f"Question 2: {res}")                
                
