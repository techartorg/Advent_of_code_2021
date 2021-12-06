from collections import deque
from copy import copy


def main():
    with open("inputs/day_06.txt", 'r') as f:
        inputs = deque([0] * 9)
        for i in f.read().split(","):
            inputs[int(i)] += 1

    print(f"Part One: {solve(inputs, 80)}")
    print(f"Part Two: {solve(inputs, 256)}")


def solve(data: deque[int], days: int) -> int:
    data = copy(data)

    for _ in range(days):
        data.rotate(-1)
        data[6] += data[8]

    return sum(data)


if __name__ == '__main__':
    main()
