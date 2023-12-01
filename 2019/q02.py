with open('q02.in') as f:
    cd = [*map(int, f.read().split(','))]

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


from copy import deepcopy
with open('q02.in') as f:
    cd = [*map(int, f.read().split(','))]

cd_ = deepcopy(cd)    


for noun in range(1,len(cd_)//4 - 1):
    for verb in range(1, len(cd_)//4 - 1):
        cd_[1] = noun
        cd_[2] = verb
        for i in range(0, len(cd_), 4):
            if cd_[i] == 99:
                #print(cd_[0])
                if cd_[0] == 19690720: 
                    print(100 * noun + verb)
                    sys.exit(0)
                cd_ = deepcopy(cd)    
                break
            elif cd_[i] == 1:
                cd_[cd_[i+3]] = cd_[cd_[i+1]] + cd_[cd_[i+2]]
            elif cd[i] == 2:
                cd_[cd_[i+3]] = cd_[cd_[i+1]] * cd_[cd_[i+2]] 
        
                
            