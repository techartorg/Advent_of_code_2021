lines = [l.strip() for l in open("day_13_input.txt") if l.strip()]
points: set[tuple[int, int]] = set()
folds: list[tuple[str, int]] = []
for line in lines:
    if line[0].isdigit():
        x, y = line.split(",")
        points.add((int(x), int(y)))
    else:
        *_, fold = line.split(" ")
        d, split = fold.split("=")
        folds.append((d, int(split)))

for idx, fold in enumerate(folds):
    axis, split = fold
    if axis == "x":
        points = {(min(x, 2 * split - x), y) for x, y in points}
    else:
        points = {(x, min(y, 2 * split - y)) for x, y in points}
    if not idx:
        print(len(points))

length: int = max(x for x, _ in points) + 1
height: int = max(y for _, y in points) + 1
grid = [[" " for _ in range(length)] for _ in range(height)]
for x, y in points:
    grid[y][x] = "#"
print("\n".join("".join(row) for row in grid))
