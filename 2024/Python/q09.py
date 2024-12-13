with open('q09.in') as f: 
    seq = [n for n in f.readline()]

    
i = 0
lst = []
available_numbers = []
an_lst = []

for ix, n in enumerate(seq): 
    if ix%2 == 0: 
        available_numbers += int(n) * [ix//2]
        an_lst.append(int(n) * str(ix//2))

available_numbers = available_numbers[::-1]
an_lst = an_lst[::-1]


stop = len(available_numbers) 

for ix, n in enumerate(seq): 
    if ix%2 == 0: 
        lst += int(n) * [ix//2] 
    else: 
        lst += available_numbers[:int(n)]
        available_numbers = available_numbers[int(n):]

print(f"Answer 1: {sum(ix*n for ix, n in enumerate(lst[:stop]))}")

class Mem():
    def __init__(b, pos, len): 
        b.pos = pos; b.len = len
    def val(b): 
        return (2*b.pos + b.len-1) * b.len // 2


pos, mem = 0, []
for len in map(int, seq):
    mem += [Mem(pos, len)]
    pos += len

for used in mem[::-2]:
    for free in mem[1::2]:
        if (free.pos <= used.pos
        and free.len >= used.len):
            used.pos  = free.pos
            free.pos += used.len
            free.len -= used.len

print(f"Answer 2: {sum(id*m.val() for id, m in enumerate(mem[::2]))}")
        
