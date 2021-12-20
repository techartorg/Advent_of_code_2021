from itertools import product
from collections import Counter

with open("day_20_input.txt") as fp:
    lookup, rest = fp.read().split("\n\n")

lookup = [str(".#".index(x)) for x in lookup]
data = {(x, y): str(".#".index(pixel)) for y, row in enumerate(rest.split("\n")) for x, pixel in enumerate(row)}
grid = list(product((-1, 0, 1), repeat=2))


def get_coordinates(d: dict[tuple[int, int], str]) -> set[tuple[int, int]]:
    return {(x + dx, y + dy) for x, y in d for dy, dx in grid}


def enhance(x: int, y: int, values: dict[tuple[int, int], str], i: int):
    # For reasons I can't entirely explain, we have to swap the default value every other pass,
    # I got this hint thanks to some people who had already solved it, it has to do with the value at the ends of the input string.
    # But I'm too tired to comprehend
    index = [values.get((x + dx, y + dy), "01"[i % 2]) for dy, dx in grid]
    return lookup[int("".join(index), 2)]


for idx in range(50):
    if idx == 2:
        print(Counter(data.values())["1"])

    data = {(x, y): enhance(x, y, data, idx) for x, y in get_coordinates(data)}

print(Counter(data.values())["1"])
