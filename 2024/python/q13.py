import re

with open('q13.in') as f: 
    rounds = f.read().split('\n\n')

# 94a + 22b = 8400
# 34a + 67b = 5400

# print((8400*67 - 5400*22) / (94*67 - 34*22)
# 94 34 22 67 8400 5400

def calc_price(part2=False): 
    total_price = 0
    for r in rounds: 
        a_x, a_y, b_x, b_y, price_x, price_y = map(int, re.findall(r'\d+', r))  
        if part2: 
            price_x += 10000000000000
            price_y += 10000000000000
        # Yay math :(
        x = (price_x*b_y - price_y*b_x) / (a_x * b_y - a_y * b_x) 
        y = (price_y - x*a_y) / b_y
        if round(x, 4).is_integer() and round(y, 4).is_integer(): 
            total_price += 3*x + y
    return int(total_price)


print(f"Answer 1: {calc_price(part2=False)}")

print(f"Answer 2: {calc_price(part2=True)}")
      

