with open('q09.in') as f: 
    seq = [n for n in f.readline()]
    
i = 0
lst = []
available_numbers = []

for ix, n in enumerate(seq): 
    if ix%2 == 0: 
        available_numbers += int(n) * [ix//2]

available_numbers = available_numbers[::-1]
stop = len(available_numbers) 

for ix, n in enumerate(seq): 
    if ix%2 == 0: 
        lst += int(n) * [ix//2] 
    else: 
        lst += available_numbers[:int(n)]
        available_numbers = available_numbers[int(n):]

print(f"Answer 1: {sum(ix*n for ix, n in enumerate(lst[:stop]))}")
