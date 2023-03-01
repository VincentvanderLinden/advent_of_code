with open('q01.in') as f: 
    src = [*map(int, f.read().splitlines())]

def find_numbers(src):
    indices = [*range(len(src))]
    for idx, value in enumerate(src):
        for i in indices:
            # Don't compare to self
            if i == idx: 
                continue
            if src[idx] + src[i] == 2020: 
                return src[idx] * src[i]

print(f"Answer 1: {find_numbers(src)}")      

def find_numbers2(src):
    indices = [*range(len(src))]
    for idx, value in enumerate(src):
        for i in indices:
            # Don't compare to self
            if i == idx: 
                continue
            for j in indices: 
                if i == j or idx == j: 
                    continue
                if src[idx] + src[i] + src[j] == 2020: 
                    return src[idx] * src[i] * src[j]

print(f"Answer 2: {find_numbers2(src)}")     