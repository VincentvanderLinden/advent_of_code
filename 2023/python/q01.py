with open('q01.in') as f: 
    texts = f.readlines()

# Part 1 
res = 0

for text in texts: 
    x = [num for num in text if num.isdigit()]
    res += int(x[0] + x[-1])

print(f"Part 1: {res}")

# Part two
import regex

number_texts = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
trans_num = lambda x: x if x.isdigit() else str(number_texts.index(x) + 1)
res = 0

for text in texts: 
    nums = regex.findall(f'\d|{"|".join(number_texts)}', text, overlapped=True)
    first, last = trans_num(nums[0]), trans_num(nums[-1])    
    res += int(first+last)

print(f"Part 2: {res}")
