from math import floor, ceil
with open('q05.in') as f:
    src = f.read().splitlines()

# Put all seats in a list

highest_seat_id = 0
all_ids = [*range(128*8)]

for plane in src: 
    chars = [*plane]
    seat = [*range(128)]
    col = [*range(8)]
    for char in chars: 
        # Rows
        if char == 'F': 
            seat = seat[0:int(len(seat)/2)]
        elif char == 'B':
            seat = seat[int(len(seat)/2):]
        # Columns    
        elif char == 'L':
            col = col[0:int(len(col)/2)]
        elif char == 'R':
            col = col[int(len(col)/2):]        
    seat_id = seat[0] * 8 + col[0]
    all_ids.remove(seat_id)
    highest_seat_id = max(seat_id, highest_seat_id)
print(f"Answer 1: {highest_seat_id}")
answer2 = [id for id in all_ids if id+1 not in all_ids and id-1 not in all_ids][0]
print(f"Answer 2: {answer2}")
