with open('q06.in') as f:
    groups = f.read().split('\n\n')

yesses = 0
all_persons_answered_yes = 0

for group in groups: 
    persons = [*group.split('\n')]
    answers = set()
    count_letters = {}
    no_of_persons = len(persons)
    for answer in persons:
        answers.update(answer)
        # Update dictionary with yesses
        for x in answer: 
            if x in count_letters.keys(): 
                count_letters[x] += 1
            else: 
                count_letters[x] = 1
    yesses += len(answers)
    # If there as many people as question answered yes, up 1
    all_persons_answered_yes += sum(value == no_of_persons for value in count_letters.values())
    
print(f"Answer 1: {yesses}")
print(f"Answer 2: {all_persons_answered_yes}")