import time

example = "x=20..30, y=-10..-5"
example = "x=85..145, y=-163..-108"
# Parse the puzzle input into some ranges so I can do containment checks
xr, yr = example.split(", ")
xr, yr = xr[2:], yr[2:]
xn, xm = map(int, xr.split(".."))
yn, ym = map(int, yr.split(".."))
xr = set(range(xn, xm + 1))
yr = set(range(yn, ym + 1))


def hits_range(dx: int, dy: int) -> tuple[bool, int]:
    x, y = (0, 0)
    max_height = 0
    while y > min(yr):
        x += dx
        y += dy
        if dx < 0:
            dx += 1
        elif dx > 0:
            dx -= 1
        dy -= 1
        max_height = max(y, max_height)
        if x in xr and y in yr:
            return True, max_height
    return False, -1


start = time.time()
valid: list[int] = []
for idx in range(max(xr) + 1):
    for jdx in range(min(yr), abs(min(yr))):
        hit, m_height = hits_range(idx, jdx)
        if hit:
            valid.append(m_height)
print(max(valid), len(valid), time.time() - start)
