from collections import Counter
from typing import Iterable

Pt = tuple[int, int]


def lerp(start: int, end: int, t: float) -> int:
    return round(start + t * (end - start))


def lerp_point(start: Pt, end: Pt, t: float) -> Pt:
    return lerp(start[0], end[0], t), lerp(start[1], end[1], t)


class Line(object):
    def __init__(self, inst: str):
        start, end = [i.split(",", maxsplit=2) for i in inst.split(" -> ", maxsplit=2)]
        self.start = (int(start[0]), int(start[1]))
        self.end = (int(end[0]), int(end[1]))

    @property
    def is_cardinal(self) -> bool:
        return any(self.start[i] == self.end[i] for i in range(2))

    @property
    def points(self) -> Iterable[Pt]:
        dx = self.end[0] - self.start[0]
        dy = self.end[1] - self.start[1]
        dist = max(abs(dx), abs(dy))

        for i in range(dist + 1):
            t = 0 if dist == 0 else i / dist
            yield lerp_point(self.start, self.end, t)


def main():
    with open("inputs/day_05.txt", 'r') as f:
        lines = [Line(i) for i in f.read().strip().splitlines()]

    print(f"Part 1: {solve(i for i in lines if i.is_cardinal)}")
    print(f"Part 2: {solve(lines)}")


def solve(lines: Iterable[Line]) -> int:
    board: Counter[Pt] = Counter()

    for line in lines:
        board.update(line.points)

    return sum(v >= 2 for v in board.values())


if __name__ == '__main__':
    main()
