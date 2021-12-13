from pathlib import Path
from typing import List, Tuple

from shapely.geometry import LineString


def part_1(data: List[Tuple[Tuple[int, int], Tuple[int, int]]]) -> None:
    lines = []
    for a, b in data:
        if a[0] == b[0] or a[1] == b[1]:
            lines.append(LineString([a, b]))
        
    intersections = 0
    for i, l in enumerate(lines):
        for j in range(i+1, len(lines)):
            if l.intersects(lines[j]):
                length = int((l.intersection(lines[j])).length)
                if length == 0:
                    length += 1
                intersections += length

    print(intersections)


def part_2(data: List[Tuple[Tuple[int, int], Tuple[int, int]]]) -> None:
    lines = []
    for a, b in data:
        if a[0] == b[0] or a[1] == b[1]:
            lines.append(LineString([a, b]))
        
    intersections = 0
    for i, l in enumerate(lines):
        for j in range(i+1, len(lines)):
            if l.intersects(lines[j]):
                length = int((l.intersection(lines[j])).length)
                if length == 0:
                    length += 1
                intersections += length

    print(intersections)


if __name__ == "__main__":
    filepath = Path(__file__).parent / "day_05_input.txt"
    raw_data = filepath.read_text().splitlines()
    data = []
    for rd in raw_data:
        data.append(tuple([(int(y), int(z)) for y,z in [x.split(',') for x in rd.split() if ',' in x]]))
    
    part_1(data) # 4826
    part_2(data) # 16793