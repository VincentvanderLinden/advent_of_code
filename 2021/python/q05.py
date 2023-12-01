import re 
with open('q05.in') as f:
    src = f.read().splitlines()


def solve(src, part): 
    line_dict = {}
    for line in src:
        # Map the coordinates
        x1, y1, x2, y2 = map(int, re.findall(r"\d+", line))
        # If it's a vertical line
        if x1 == x2:
            # fill the coordinates of the line  
            for coord in range(min(y1, y2), max(y1, y2) + 1):
                if (x1, coord) not in line_dict.keys(): 
                    line_dict[(x1, coord)] = 1
                else: 
                    line_dict[(x1, coord)] += 1
        elif y1 == y2: 
            for coord in range(min(x1, x2), max(x1, x2)+1):
                if (coord, y1) not in line_dict.keys(): 
                    line_dict[(coord, y1)] = 1
                else: 
                    line_dict[(coord, y1)] += 1
        if part == 1:
            continue
        # Diagonal
        elif part == 2:
            if x1 != x2 and y1 != y2:
                for idx, coord in enumerate(range(min(x1, x2), max(x1, x2)+1)):
                    # Determine correct direction
                    if x1 < x2: 
                        x = x1+idx
                    else: 
                        x = x1-idx 
                    if y1 < y2: 
                        y = y1+idx
                    else: 
                        y = y1-idx
                    if (x, y) not in line_dict.keys(): 
                        line_dict[(x, y)] = 1
                    else: 
                        line_dict[(x, y)] += 1
    return line_dict


# Print out the length of the list containing 'unique duplicates'
lines = solve(src, 1)
print(f"Answer 1: {len([i for i in lines if lines[i] > 1])}")

# Part 2:
lines = solve(src, 2)
print(f"Answer 1: {len([i for i in lines if lines[i] > 1])}")


