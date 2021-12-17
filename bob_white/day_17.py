example = "x=20..30, y=-10..-5"
example = "x=85..145, y=-163..-108"
# Parse the puzzle input into some ranges so I can do containment checks
_x_range, _y_range = example.split(", ")
_x_range, _y_range = _x_range[2:], _y_range[2:]
x_min, x_max = map(int, _x_range.split(".."))
y_min, y_max = map(int, _y_range.split(".."))
x_range = set(range(x_min, x_max + 1))
y_range = set(range(y_min, y_max + 1))


def hits_range(dx: int, dy: int) -> tuple[bool, int]:
    x, y = (0, 0)
    max_height = 0
    while y > y_min and x <= x_max:
        x += dx
        y += dy
        if dx < 0:
            dx += 1
        elif dx > 0:
            dx -= 1
        dy -= 1
        if y > max_height:
            max_height = y
        if x in x_range and y in y_range:
            return True, max_height
    return False, -1


valid: list[int] = []
for x in range(x_max + 1):
    for y in range(y_min, abs(y_min)):
        hit, m_height = hits_range(x, y)
        if hit:
            valid.append(m_height)
print(max(valid), len(valid))
