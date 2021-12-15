from itertools import product

start = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526""".split(
    "\n"
)


def get_surrounding(x: int, y: int) -> list[tuple[int, int]]:
    return [coords for dx, dy in product((-1, 0, 1), (-1, 0, 1)) if (coords := ((x + dx), (y + dy))) in grid]


grid = {(x, y): int(v) for y, row in enumerate(open("day_11_input.txt").read().split("\n")) for x, v in enumerate(row)}
# grid = {(x, y): int(v) for y, row in enumerate(start) for x, v in enumerate(row)}

total = 0
for step in range(1, 500):

    for oct in grid:
        grid[oct] += 1
    flash: set[tuple[int, int]] = {oct for oct in grid if grid[oct] > 9}
    flashed: set[tuple[int, int]] = set()
    while flash:
        oct = flash.pop()
        if oct in flashed:
            continue
        for surrounding_oct in get_surrounding(*oct):
            grid[surrounding_oct] += 1
            if grid[surrounding_oct] > 9:
                flash.add(surrounding_oct)
        flashed.add(oct)
    for oct in flashed:
        grid[oct] = 0
    total += len(flashed)
    if step == 100:
        print(total)
    if all(v == 0 for v in grid.values()):
        print(step)
        break
