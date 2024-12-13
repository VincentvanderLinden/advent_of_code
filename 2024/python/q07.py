with open('q07.in') as f: 
    inp = [line.strip() for line in f.readlines()]

R=0
for line in inp: 
    result = int(line.split(':')[0])
    items = [int(l) for l in line.split(':')[1].split()]
    res = [items[0]]
    for i in range(1, len(items)): 
        for j in res[-1*(2**i):]:
            res.append(j + items[i])
            res.append(j * items[i])
            
    if result in res[-1*(2**i):]: 
        R+=result

print(f"Part 1: {R}")


# Brute forcing in batches, running 100 at a time </shame>             
R = 0
for line in inp[:100]: 
    result = int(line.split(':')[0])
    items = [int(l) for l in line.split(':')[1].split()]
    res = [items[0]]
    for i in range(1, len(items)): 
        for j in res[-1*(3**i):]:
            res.append(j + items[i])
            res.append(j * items[i])
            res.append(int(str(j) + str(items[i])))

    if result in res[-1*(3**i):]: 
        R+=result
print(f"Part 2 (PARTIAL): {R}")
