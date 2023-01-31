with open('q11.in') as file:
    input = file.read().split('\n\n')

monkeys = [line.split('\n') for line in input]

print(monkeys)