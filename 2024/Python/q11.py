from collections import Counter
from functools import cache
import utils

with open('q11.in') as f:
    inp = [int(n) for n in f.readline().split()]

# print(count_even_lengths(inp))
YEAR = 2024


@cache
def process_value(val: int) -> list:
    if val == 0:
        result = [1]
    elif len(str(val)) % 2 == 0:
        mid = len(str(val)) // 2
        left_half = int(str(val)[:mid])
        right_half = int(str(val)[mid:])
        result = [left_half, right_half]
    else:
        result = [val * YEAR]

    return result

@cache
def fast_blink(stone: int, blinks: int) -> int:
    if blinks == 0:
        return 1

    transformed_stones = process_value(stone)
    return sum(fast_blink(num, blinks - 1) for num in transformed_stones)


@utils.timeit
def run(inp, times):
    total = 0
    for stone in inp:
        total += fast_blink(stone, times)
    return total


print(f"Answer 1: {run(inp, 25)}")
print(f"Answer 2: {run(inp, 75)}")
