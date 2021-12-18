from __future__ import annotations

import re
from itertools import product
from typing import NamedTuple

input_pattern = re.compile(r"\w=(-?\d+)\.\.(-?\d+)")


class Pt(NamedTuple):
    x: int
    y: int

    def __add__(self, rhs: Pt):
        return Pt(self.x + rhs.x, self.y + rhs.y)

    def __sub__(self, rhs: Pt):
        return Pt(self.x - rhs.x, self.y - rhs.y)


class Rect(object):
    def __init__(self, x_range: tuple[int, int], y_range: tuple[int, int]):
        self.min: Pt = Pt(x_range[0], y_range[0])
        self.max: Pt = Pt(x_range[1], y_range[1])

    def __contains__(self, point: Pt) -> bool:
        in_x = self.min.x <= point.x <= self.max.x
        in_y = self.min.y <= point.y <= self.max.y
        return in_x and in_y


def main():
    with open("inputs/day_17.txt", 'r') as f:
        area = Rect(*[tuple(int(j) for j in i) for i in input_pattern.findall(f.read())])

    print(f"Part One: {area.min.y * (area.min.y + 1) // 2}")  # triangle numbers

    hits = [r for v in product(range(area.max.x + 1), range(area.min.y, -area.min.y)) if (r := solve(Pt(*v), area)) is not None]
    print(f"Part Two: {len(hits)}")


def sign(n: int) -> int:
    if n == 0:
        return 0
    return 1 if n >= 0 else -1


def solve(velocity: Pt, area: Rect) -> int | None:
    point = Pt(0, 0)
    max_y = 0

    while True:
        point += velocity

        # under target
        if point.y < area.min.y:
            return None

        velocity -= Pt(sign(velocity.x), 0)
        velocity -= Pt(0, 1)
        max_y = max(max_y, point.y)

        if point in area:
            return max_y


if __name__ == '__main__':
    main()
