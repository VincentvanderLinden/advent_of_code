with open('q09.in') as f: 
    nums = [int(number) for number in f.read().splitlines()]

# Set current position and offset
current_position = 26
offset = 25

# Loop through the previous 5 numbers for part 1
while current_position < len(nums):
    for i in nums[current_position - offset - 1: current_position]:
        valid = False
        # loop through the previous 5 numbers minus i
        for j in nums[current_position - offset -1 : current_position]:
            # print(nums[current_position], i, j)
            # Ignore ourself :)
            if i == j:
                pass
            # Check if the sum of two numbers == the number of current_position
            elif i + j == nums[current_position]: 
                valid = True
                # break, we know it's valid
                break
        if valid: 
            # break, we know it's valid
            break
    # If no valid sums are found, we reached the answer
    if not valid: 
        print("Answer 1: ", nums[current_position])
        target = nums[current_position]
        break
    # Otherwise move on to the next position
    current_position += 1
    

# Find a contiguous set
# Start with set size of 2
cont_set_size = 2
current_position = 0
valid = False 

# Go through the numbers, trying to find the target set in part 1
while current_position < len(nums) + cont_set_size and len(nums) > cont_set_size: 
    for i in nums: 
        # If the sum of the set equals the target, print answer and break out
        if sum(nums[current_position:current_position+cont_set_size]) == target:
            found_set = nums[current_position:current_position+cont_set_size]
            print('Answer 2: ', min(found_set) + max(found_set))
            valid = True
            # break, we know it's valid
            break
        current_position += 1
    if valid: 
        # break, we know it's valid
        break    
    # Otherwise: reset current position and try it with a larger list
    else: 
        current_position = 0
        cont_set_size += 1
    
    

