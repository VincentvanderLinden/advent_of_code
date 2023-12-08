import re
from collections import deque, defaultdict

with open('q04.in') as f: 
    cards = f.read().splitlines()


def check_win(card): 
    ticket, result = card.split(': ')[1].split(' | ')
    ticket = re.findall('\d+', ticket)
    result = re.findall('\d+', result)
    return sum([1 for x in ticket if x in result])

no_of_cards = len(cards)
card_stack = defaultdict(lambda: 1)
answer1 = 0

for card_no, card in enumerate(cards):
    matches = check_win(card)
    answer1 += 2**(int(matches)-1) if matches > 0 else 0
    for i in range(card_no + 1, min(card_no+matches+1, no_of_cards)): 
        card_stack[i] += card_stack[card_no]  

print(f'Answer 1: {answer1}')
print(f'Answer 2: {sum(card_stack.values()) + (no_of_cards - len(card_stack))}')
