with open('q02.in') as f:
    cd = [*map(int, f.read().split(','))]

print(cd)
# Change input
cd[1] = 12
cd[2] = 2

# Split into pairs of four
for i in range(0, len(cd), 4):
    if cd[i] == 99:
        break
    elif cd[i] == 1:
        cd[cd[i+3]] = cd[cd[i+1]] + cd[cd[i+2]]
    elif cd[i] == 2:
        cd[cd[i+3]] = cd[cd[i+1]] * cd[cd[i+2]]    

print(f"Answer 1: {cd[0]}")


