with open('q05.in') as f: 
    ranges, ingredients = input = f.read().split('\n\n')
    ranges, ingredients = ranges.split('\n'), map(int, ingredients.split('\n'))
    
answer1 = 0
for ingredient in ingredients: 
    fresh = False    
    for range in ranges: 
        low, high = map(int, range.split('-'))
        if low <= ingredient <= high: 
            fresh = True
            answer1 += 1
            break 
print(f"Answer 1: {answer1}")

# Part 2: 

answer2 = 0
all_ranges = [(int(a), int(b)) for a, b in [range.split('-') for range in ranges]]

# Sort by lower range bound
all_ranges.sort(key=lambda x: x[0])
ranges_seen = []

for low, high in all_ranges: 
    # First range
    if not ranges_seen: 
        ranges_seen.append((low, high))
    else: 
        last_range_low, last_range_high = ranges_seen[-1]       
        # If lower bound is in last range
        if last_range_low <= low <= last_range_high:
            # Only extend if high is higher than last high
            if high >= last_range_high: 
                ranges_seen[-1] = (last_range_low, high)
        # else just add new range             
        else: 
            ranges_seen.append((low, high))

for rs in ranges_seen: 
    answer2 += rs[1] - rs[0] + 1
    
print(f"Answer 2: {answer2}")

    
    
    
    