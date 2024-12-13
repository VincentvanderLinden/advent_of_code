import re

with open('q03.in') as f: 
    line = f.read()

muls = re.findall("mul\(\d+,\d+\)", line)

def calc_mul(mul): 
    nums = [int(num) for num in re.findall("\d+", mul)]
    return nums[0] * nums[1] if len(nums) == 2 else 0 

res = 0
for mul in muls: 
    res += calc_mul(mul)

print(f"Question 1: {res}")

spl = re.split("(don\'t\(\)|do\(\))", line)

res = 0
for i in range(len(spl)):
    if i == 0: 
        if spl[i] != "don\'t()": 
            muls = re.findall("mul\(\d+,\d+\)", spl[i])
            for mul in muls: 
                res += calc_mul(mul)
           
    elif spl[i-1] == "don\'t()": 
            continue
    else: 
        muls = re.findall("mul\(\d+,\d+\)", spl[i])
        for mul in muls: 
            res += calc_mul(mul)
    
print(f"Question 2: {res}")
      
    
