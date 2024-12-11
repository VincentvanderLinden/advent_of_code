with open('q11.in') as f: 
    inp = [n for n in f.readline().split()]

def count_even_lengths(lst: list) -> int: 
    return sum([1 for n in lst if len(n)%2 == 0])

#print(count_even_lengths(inp))    
YEAR = 2024

def blink(lst: list) -> list:
    new_list = []
    for e in lst: 
        if e == '0':
            new_list.append('1')
        elif len(e)%2 == 0: 
            new_list += [str(int(e[:len(e)//2])), str(int(e[len(e)//2:]))]
        else: 
            new_list.append(str(int(e) * YEAR))
    return new_list
        
for n in range(20): 
    
    if n == 0: 
        prev_l = len(inp)
        l = blink(inp)
        new_l = len(l)
    else: 
        prev_l = len(l)
        l = blink(l)
        new_l = len(l)
    print(f"{prev_l=}, {new_l=}, {new_l - prev_l=}")
print(f"Answer 1: {len(l)}")
