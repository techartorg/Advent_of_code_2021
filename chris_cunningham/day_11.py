import itertools
from typing import Iterable

Grid = list[list[int]]
Pt = tuple[int, int]


def main():
    with open("inputs/day_11.txt", 'r') as f:
        inputs = [[int(i) for i in row] for row in f.read().splitlines()]

    print(f"Part One: {part_one(inputs[:])}")
    print(f"Part Two: {part_two(inputs[:])}")


def grid_iter(grid: Grid) -> Iterable[Pt]:
    for r, row in enumerate(grid):
        for c, _ in enumerate(row):
            yield r, c


def get_neighbors(grid: Grid, row: int, col: int) -> Iterable[Pt]:
    row_len, col_len = len(grid), len(grid[0])

    for r, c in itertools.product((-1, 0, 1), (-1, 0, 1)):
        if (r, c) == (0, 0):
            continue

        nr, nc = row + r, col + c
        if 0 <= nr < row_len and 0 <= nc < col_len:
            yield nr, nc


def solve_step(grid: Grid) -> int:
    stack = [*grid_iter(grid)]
    flashed = set()
    count = 0

    while stack:
        row, col = stack.pop()
        if (row, col) in flashed:
            continue

        grid[row][col] += 1

        if grid[row][col] > 9:
            count += 1
            flashed.add((row, col))
            grid[row][col] = 0
            stack.extend(get_neighbors(grid, row, col))

    return count


def part_one(grid: Grid) -> int:
    return sum(solve_step(grid) for _ in range(100))


def part_two(grid: Grid) -> int:
    for step in itertools.count(1):
        if solve_step(grid) == 100:
            return step


if __name__ == '__main__':
    main()
