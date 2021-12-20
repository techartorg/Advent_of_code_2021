import copy
from itertools import chain
from pathlib import Path
from typing import List, Tuple


def _do_flash(grid: List[List[int]], flashpoints: List[Tuple[int, int]], to_zero: List[Tuple[int, int]]) -> Tuple[List[List[int]], int]:
    new_flashpoints = []
    to_zero.extend(flashpoints)
    for r, c in flashpoints:
        for coord in [ (r - 1, c - 1), (r - 1, c), (r - 1, c + 1),
                       (r, c - 1), (r, c + 1),
                       (r + 1, c - 1), (r + 1, c), (r + 1, c + 1)]:
            r_1, c_1 = coord
            if r_1 < 0 or r_1 > len(grid) - 1:
                continue
            if c_1 < 0 or c_1 > len(grid[0]) - 1:
                continue
            
            val = grid[r_1][c_1]
            if val == -1:
                continue
            val = -1 if val == 9 else val + 1
            if val == -1:
                new_flashpoints.append((r_1, c_1))
            grid[r_1][c_1] = val

    if new_flashpoints:
        return _do_flash( grid, new_flashpoints, to_zero)

    for r, c in to_zero:
        grid[r][c] = 0

    return grid, len(to_zero)


def part_1(grid: List[List[int]]) -> None:
    num_flashes = 0

    for _s in range(100):
        flashpoints = []

        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                val = val + 1 if val <= 8 else -1
                grid[r][c] = val
                if val == -1:
                    flashpoints.append((r,c))

        if flashpoints:            
            grid, flash_count = _do_flash(grid, flashpoints, [])
            num_flashes += flash_count
        
    print(num_flashes)


def part_2(grid: List[List[int]]) -> None:
    step = 1
    while True:

        flashpoints = []

        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                val = val + 1 if val <= 8 else -1
                grid[r][c] = val
                if val == -1:
                    flashpoints.append((r,c))

        if flashpoints:            
            grid, _fc = _do_flash(grid, flashpoints, [])

        if all([not x for x in list(chain(*grid))]):
            print(step)
            return

        step += 1


if __name__ == "__main__":
    filepath = Path(__file__).parent / "day_11_input.txt"
    data = filepath.read_text().splitlines()
    grid = []
    for d in data:
        grid.append([int(x) for x in d])
    
    part_1(copy.deepcopy(grid))
    part_2(grid)
