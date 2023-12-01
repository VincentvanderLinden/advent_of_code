import re

with open('q07.in') as f:
    src = f.read().splitlines()

bag_dict = {}
for line in src: 
    main_bag = re.findall(r"\w+ \w+(?= bags contain)", line)
    sub_bags = re.findall(r"\d+ \w+ \w+(?= bag)", line)
    bag_dict[main_bag[0]] = {re.findall(r"(?<=\d )\w+ \w+", bag)[0]: int(re.findall(r"\d+", bag)[0]) for bag in sub_bags}


def find_bag(dict, str, bag_set): 
    for key, value in dict.items(): 
        if str in value:
            bag_set.add(key)
            find_bag(dict, key, bag_set)
    return bag_set

bag_set = set()
print(f"Answer 1: {len(find_bag(bag_dict, 'shiny gold', bag_set))}")

def get_no_of_bags(dict, str, multiplier): 
    for key, value in dict[str].items(): 
        if value:
            if key in bag_set: 
                bag_set[key] += value * multiplier 
            else: 
                bag_set[key] = value * multiplier
            get_no_of_bags(dict, key, value * multiplier)    
    return bag_set

bag_set = {}
print(f"Answer 2: {sum(get_no_of_bags(bag_dict, 'shiny gold', 1).values())}")
