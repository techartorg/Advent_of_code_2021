from copy import copy
from operator import ge, lt
from typing import Callable


def main():
    inputs = [int(i, 2) for i in open("inputs/day_03.txt", 'r').read().strip().splitlines()]
    print(f"Part One: {part_one(inputs)}")
    print(f"Part Two: {part_two(inputs)}")


def part_one(inputs: list[int]) -> int:
    half = len(inputs) / 2
    gamma = 0

    for pos in range(12):
        count = sum((i & (1 << pos)) > 0 for i in inputs)
        if count > half:
            gamma += 1 << pos

    epsilon = ~gamma & 0xfff
    return gamma * epsilon


def part_two(inputs: list[int]) -> int:
    oxy = get_reading(inputs, ge)
    co2 = get_reading(inputs, lt)
    return co2 * oxy


def get_reading(inputs: list[int], predicate: Callable[[int, int], bool]) -> int:
    data = copy(inputs)

    for pos in reversed(range(12)):
        ones = sum((i & (1 << pos)) > 0 for i in data)
        mask = 1 if predicate(ones, len(data) - ones) else 0
        data = [i for i in data if (i >> pos) & 1 == mask]
        if len(data) == 1:
            break

    return data[0]


if __name__ == '__main__':
    main()
