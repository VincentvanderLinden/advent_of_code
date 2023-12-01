import re

with open('q07.in') as file:
    src = file.readlines()

# Use list to track current position in the file system
# and to make sure you can add file sizes to parents
current_dir = []
# Use a dict to store file sizes per directory
file_system = {}

for line in src:
    # Throw away garbage
    if line.startswith('$ ls') | line.startswith('dir'):
        continue
    # Directory changes with cd
    elif line.startswith('$ cd'):
        # E.g. $ cd a, a will be the target. In case of $ cd .., pop one value from list.
        target = line.split()[2]
        if target == '..':
            current_dir.pop()
        else:
            current_dir.append(target)
    # Files start with digits
    elif re.match(r"^\d+", line):
        file_size = int(line.split()[0])
        # Use strings as dict keys
        # Add size of files to directory and all parent directories
        # If current dir is /a/b/c, add file_size to /a/b/c, /a/b, /a and /
        for path in ['/'.join(current_dir[0:n+1]) for n in range(0, len(current_dir))]:
            # If the path already exists, add it to the total file_size
            if path in file_system:
                file_system[path] = file_system[path] + file_size
            # If the path does not exist, create it using path as a dict key
            else:
                file_system[path] = file_size
    else:
        raise Exception(f"Unknown unix command: {line}. Please fix the input file or add handling for the command.")
# Calculate and print answer
answer1 = sum([value for value in file_system.values() if value <= 100000])
print(f"answer 1: {answer1}")

# Part two. Set up some variables
total_disk_size = 7e7
needed_space = 3e7
current_free_space = total_disk_size - file_system['/']
space_to_free_up = needed_space - current_free_space
# Filter the dictionary for all directories larger than the needed space
filtered_list = filter(lambda size: size >= space_to_free_up, file_system.values())
# Answer is the first value from the sorted list of values remaining
print(f"answer 2: {sorted(filtered_list)[0]}")
