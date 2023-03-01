import re
with open('q02.in') as f: 
    src = f.read().splitlines()

valid = 0    
for pw in src: 
    at_least = int(re.findall(r"\d+", pw)[0])
    at_most = int(re.findall(r"\d+", pw)[1])
    letter = re.findall(r"\w(?=:)", pw)[0]
    password = re.findall(r"(?<=: )\w+", pw)[0]
    if at_least <= password.count(letter) <= at_most:
        valid += 1
   
print(f"Answer 1: {valid}")

valid = 0    
for pw in src: 
    first_pos = int(re.findall(r"\d+", pw)[0])
    second_pos = int(re.findall(r"\d+", pw)[1])
    letter = re.findall(r"\w(?=:)", pw)[0]
    password = re.findall(r"(?<=: )\w+", pw)[0]
    # True + False = 1
    if (password[first_pos - 1] == letter) + (password[second_pos - 1] == letter) == 1: 
        valid += 1

print(f"Answer 2: {valid}")