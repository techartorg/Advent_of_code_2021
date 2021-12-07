import sys
from typing import Callable


def g_dist(a: int, b: int) -> int:
    distance = abs(a - b)
    return distance * (distance + 1) // 2


def main():
    with open("inputs/day_07.txt", 'r') as f:
        inputs = [int(i) for i in f.read().split(",")]
        print("".join(chr(i) for i in inputs))  # wish it was

    print(f"Part One: {solve(inputs, lambda a, b: abs(a - b))}")
    print(f"Part Two: {solve(inputs, g_dist)}")


def solve(inputs: list[int], cost_exp: Callable[[int, int], int]):
    min_cost = sys.maxsize

    for i in range(min(inputs), max(inputs) + 1):
        cost = sum(cost_exp(v, i) for v in inputs)
        min_cost = min(min_cost, cost)

    return min_cost


if __name__ == '__main__':
    main()
