import re

l, r = [], []
with open('q01.in') as f: 
    inp = f.read().splitlines()

for i in inp: 
    nums = re.findall('\d+', i)
    l.append(int(nums[0]))
    r.append(int(nums[1]))

q1 = sum(abs(a-b) for a, b in zip(sorted(l), sorted(r)))
print(f"Question 1: {q1}")

q2 = 0
for num in l: 
    q2 += num*r.count(num)

print(f"Question 1: {q2}")
