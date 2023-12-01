with open('q01.in') as f:
    txt = f.read()

# Part 1
print(f"Answer 1: {txt.count('(') - txt.count(')')}")

# Part 2