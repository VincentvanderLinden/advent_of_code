import itertools

with open("q03.in") as f: 
    input = f.read().splitlines()
    

 
def part1(input: list) -> int:   
    joltage = 0
    for line in input: 
        bank = list(line)
        
        # Get highest number, but not last position
        ix1 = bank.index(max(bank[:-1]))
        d1 = bank[ix1]
        bank.pop(ix1)
        
        # Get highest number after previous highest number
        ix2 = bank.index(max(bank[ix1:]))
        d2 = bank[ix2]
        joltage += int(d1+d2)
    return joltage

print(f"Answer 1: {part1(input)}")

def part2(input: list) -> int:   
    
    result = 0
    
    for line in input: 

        joltage = ''
        num_of_batteries = 12
        
        bank = list(line)
        search_window = len(bank) - num_of_batteries + 1
        
        while len(joltage) < num_of_batteries: 
        
            high_ix = bank.index(max(bank[:search_window]))
            joltage += bank[high_ix]
            bank = bank[high_ix+1:]
            search_window = len(bank) - num_of_batteries + len(joltage) + 1
        
        result += int(joltage)
        
    return result

print(f"Part 2: {part2(input)}")
