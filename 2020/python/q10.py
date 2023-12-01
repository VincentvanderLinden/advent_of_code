with open('q10.in') as f:
    # Sort them by joltage
    adapters = sorted([int(x) for x in f.read().splitlines()])

# Set starting conditions

# Check first adapter
diff_1jolt = 1 if adapters[0] == 1 else 0
diff_3jolt = 1 if adapters[0] > 1 else 0

# Loop up until last adapter
for idx, adapter in enumerate(adapters[:-1]): 
    if adapters[idx + 1] - adapter == 1:
        diff_1jolt += 1
    elif adapters[idx + 1] - adapter == 3:
        diff_3jolt += 1
# Add 3 joltage to reach device joltage
diff_3jolt += 1

print("Answer 1:", diff_1jolt * diff_3jolt)

# Part two: Pathfinding?
route = []
visited_list = set()
unique_routes = 0
for idx, adapter in enumerate(adapters[:-1]): 
    if adapters[idx + 1] - adapter in [1, 3]:
        route.append(adapter) 
        visited_list.update(route)

print(visited_list)
    
