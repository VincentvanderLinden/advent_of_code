def calc_fuel(mass):
    return mass//3 - 2

with open('q01.in') as f:
    modules = [*map(int, f.read().splitlines())]

print(f"Answer 1: {sum([calc_fuel(mass) for mass in modules])}")


def spend_fuel(mass): 
    fuel = 0
    while calc_fuel(mass) > 0:
        mass = calc_fuel(mass)
        fuel += mass 
    return(fuel)

print(f"Answer 2: {sum([spend_fuel(mass) for mass in modules])}")