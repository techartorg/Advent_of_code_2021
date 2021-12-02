from contextlib import suppress
from pathlib import Path
from typing import List

# Must be using Python 3.1x for this to work.

def part_1(data: List[str]) -> None:
    pos = 0
    depth = 0
    for d in data:
        command, val = d.split(' ')
        match command:
            case "forward":
                pos += int(val)
            case "up":
                depth -= int(val)
            case "down":
                depth += int(val)
    
    print(pos * depth)


def part_2(data: List[str]) -> None:
    aim = 0
    pos = 0
    depth = 0
    for d in data:
        command, val = d.split(' ')
        match command:
            case "forward":
                pos += int(val)
                depth += (aim * int(val))
            case "up":
                aim -= int(val)
            case "down":
                aim += int(val)

    print(pos * depth)


if __name__ == "__main__":
    filepath = Path(__file__).parent / "day_02_input.txt"
    data = filepath.read_text().split("\n")
    part_1(data)
    part_2(data)
