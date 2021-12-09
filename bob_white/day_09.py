import math

grid = [
    [int(v) for v in line]
    for line in """2199943210
3987894921
9856789892
8767896789
9899965678""".split(
        "\n"
    )
]
grid = [[int(v) for v in line] for line in open("day_09_input.txt").read().split("\n")]


def get_neighboring_coords(grid: list[list[int]], x: int, y: int) -> set[tuple[int, int]]:
    vals: set[tuple[int, int]] = set()
    neighbors = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for dx, dy in neighbors:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid):
            vals.add((nx, ny))
    return vals


def get_neighboring_values(grid: list[list[int]], x: int, y: int) -> list[int]:
    return [grid[y][x] for x, y in get_neighboring_coords(grid, x, y)]


def breadth_search(grid: list[list[int]], visited: set[tuple[int, int]], x: int, y: int) -> set[tuple[int, int]]:
    visited.add((x, y))
    for dx, dy in get_neighboring_coords(grid, x, y):
        if grid[dy][dx] == 9 or (dx, dy) in visited:
            continue
        visited.add((dx, dy))
        visited.update(breadth_search(grid, visited, dx, dy))
    return visited


total = 0
for y, row in enumerate(grid):
    for x, v in enumerate(row):
        vals: list[int] = get_neighboring_values(grid, x, y)
        if all(val > v for val in vals):
            total += v + 1
print(total)


visited: set[tuple[int, int]] = set()
basins: list[int] = []
for y, row in enumerate(grid):
    for x, v in enumerate(row):
        if v == 9 or (x, y) in visited:
            continue
        # Don't be a moron and feed it the existing visited set, we want to start fresh each time.
        basin = breadth_search(grid, set(), x, y)
        visited.update(basin)
        basins.append(len(basin))
# Get the top 3, and multiply them together
vals = sorted(basins, reverse=True)[:3]
print(math.prod(vals))
