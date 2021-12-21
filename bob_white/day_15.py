from heapq import heapify, heappop, heappush

example = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581""".split(
    "\n"
)

grid = {(x, y): int(v) for y, line in enumerate(example) for x, v in enumerate(line)}
grid = {(x, y): int(v) for y, line in enumerate(open("day_15_input.txt")) for x, v in enumerate(line) if v.isdigit()}


def get_neighbors(pnt: tuple[int, int]) -> list[tuple[int, int]]:
    x, y = pnt
    return [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]


# A* time! heapq isn't something I use often, but damn if it isn't perfect for this
seen: set[tuple[int, int]] = set()
start = (0, 0)
finish = tuple(map(max, zip(*grid)))
paths = [(0, (0, 0))]
heapify(paths)
while True:
    danger, pnt = heappop(paths)
    if pnt in seen:
        continue
    seen.add(pnt)
    if pnt == finish:
        print(danger)
        break
    for v in get_neighbors(pnt):
        if v not in grid or v in seen:
            continue
        heappush(paths, (danger + grid[v], v))

# Grow the grid, this is such terrible code
for xdx in range(0, 500):
    x = xdx - 100
    for y in range(0, 100):
        if (x, y) not in grid:
            continue
        v = grid[(x, y)]
        v += 1
        if v == 10:
            v = 1
        grid[(xdx, y)] = v
# No seriously, this code is awful
for ydx in range(0, 500):
    y = ydx - 100
    for x in range(0, 500):
        if (x, y) not in grid:
            continue
        v = grid[(x, y)]
        v += 1
        if v == 10:
            v = 1
        grid[(x, ydx)] = v
# Reset for part 2, this should probably be a function
seen: set[tuple[int, int]] = set()
start = (0, 0)
finish = tuple(map(max, zip(*grid)))
paths = [(0, (0, 0))]
heapify(paths)
while True:
    danger, pnt = heappop(paths)
    if pnt in seen:
        continue
    seen.add(pnt)
    if pnt == finish:
        print(danger)
        break
    for v in get_neighbors(pnt):
        if v not in grid or v in seen:
            continue
        heappush(paths, (danger + grid[v], v))
