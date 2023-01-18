with open ('q02.in') as f:
    input = f.read().splitlines()

#Rock: X, Paper: Y, Scissors: Z
#Create dict of action: reaction
action_reaction = [{'action': line[0], 'reaction': line[2]} for line in input]
#Base scores for picking an reaction
base_score = {'X': 1, 'Y': 2, 'Z': 3}
#Create scoring dict
scoring = {'A': {'X': 3, 'Y': 6, 'Z': 0}, 
           'B': {'X': 0, 'Y': 3, 'Z': 6}, 
           'C': {'X': 6, 'Y': 0, 'Z': 3},
          }

#ANSWER PART 1:
#Translate action list using scoring dict, adding the outcome score + the base score
sum([scoring[line['action']][line['reaction']] + 
     base_score[line['reaction']] 
     for line in action_reaction])

#Part 2
#X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win
action_to_take = {'X': {'A': 'Z', 'B': 'X', 'C': 'Y'}, 
                  'Y': {'A': 'X', 'B': 'Y', 'C': 'Z'}, 
                  'Z': {'A': 'Y', 'B': 'Z', 'C': 'X'},
                 }

#Using for loop for legibility
#Determine which action will be taken and use that to calculate score
#using the scoring table defined before
score = 0
for line in action_reaction: 
    action_taken = action_to_take[line['reaction']][line['action']]
    score += scoring[line['action']][action_taken] + base_score[action_taken] 
#ANSWER PART 2:
score
