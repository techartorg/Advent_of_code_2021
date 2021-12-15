from math import prod
from typing import Iterable

_test_input = """2199943210
3987894921
9856789892
8767896789
9899965678"""


def main():
    # inputs = [[int(c) for c in line] for line in _test_input.splitlines()]
    with open("inputs/day_09.txt", 'r') as f:
        inputs = [[int(c) for c in line] for line in f.read().splitlines()]

    lows = part_one(inputs)
    print(f"Part One: {sum(i[2] + 1 for i in lows)}")
    print(f"Part Two: {part_two(inputs, lows)}")


def get_neighbors(grid: list[list[int]], row: int, col: int) -> Iterable[tuple[int, int]]:
    row_len, col_len = len(grid), len(grid[0])

    for r, c in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        nr, nc = row + r, col + c

        if 0 <= nr < row_len and 0 <= nc < col_len:
            yield nr, nc


def part_one(inputs: list[list[int]]) -> list[tuple[int, int, int]]:
    lows = []

    for row, line in enumerate(inputs):
        for col, value in enumerate(line):
            if value == 9:
                continue

            if all(inputs[nr][nc] > value for nr, nc in get_neighbors(inputs, row, col)):
                lows.append((row, col, value))

    return lows


def part_two(grid: list[list[int]], lows: Iterable[tuple[int, int, int]]) -> int:
    basin_sizes = []
    basins = []

    for row, col, value in lows:
        visited = set()
        queue = [(row, col)]

        while queue:
            row, col = queue.pop()

            if (row, col) in visited:
                continue

            visited.add((row, col))

            for nr, nc in get_neighbors(grid, row, col):
                n_value = grid[nr][nc]

                if n_value == 9 or value >= n_value:
                    continue

                queue.append((nr, nc))

        basin_sizes.append(len(visited))
        basins.append(visited)

    return prod(sorted(basin_sizes, reverse=True)[:3])


if __name__ == '__main__':
    main()
