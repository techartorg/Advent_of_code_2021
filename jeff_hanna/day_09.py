from math import prod
from pathlib import Path
from typing import List, Set, Tuple


def _find_adjoining_coords(data: List[List[int]], x: int, y: int) -> Set[Tuple[int, int]]:
    values = set()

    adjoining = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for x1, y1 in adjoining:
        x2, y2 = x + x1, y + y1
        if 0 <= x2 < len(data[0]) and 0 <= y2 < len(data):
            values.add((x2, y2))
    
    return values


def _find_adjoining_values(data: List[List[int]], x:int, y:int) -> List[int]:
    return [data[y][x] for x, y in _find_adjoining_coords(data, x, y)]


def _bfs(data: List[List[int]], x: int, y: int, visited_locs: Set[Tuple[int, int]]) -> Set[Tuple[int, int]]:
    visited_locs.add((x, y))
    for x1, y1 in _find_adjoining_coords(data, x, y):
        if data[y1][x1] == 9 or (x1, y1) in visited_locs:
            continue

        visited_locs.add((x1, y1))
        visited_locs.update(_bfs(data, x1, y1, visited_locs))

    return visited_locs    


def part_1(data: List[List[int]]) -> None:
    total = 0
    for y, row in enumerate(data):
        for x, v in enumerate(row):
            if all(z > v for z in _find_adjoining_values(data, x, y)):
                total += v + 1

    print(total)


def part_2(data: List[List[int]]) -> None:
    visited_locs = set()
    basins = []
    for y, row in enumerate(data):
        for x, v in enumerate(row):
            if v == 9 or (x, y) in visited_locs:
                continue

            basin = _bfs(data, x, y, set())
            visited_locs.update(basin)
            basins.append(len(basin))
    
    print(prod(sorted(basins, reverse = True)[:3]))


if __name__ == "__main__":
    filepath = Path(__file__).parent / "day_09_input.txt"
    data = [[int(y) for y in x] for x in filepath.read_text().splitlines()]
    part_1(data)
    part_2(data)
