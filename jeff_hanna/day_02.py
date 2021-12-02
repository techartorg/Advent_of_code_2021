from contextlib import suppress
from pathlib import Path
from typing import List


def part_1(data: List[str]) -> None:
    total = sum([int(x.split(' ')[-1]) for x in data if x.startswith("forward")]) * \
            ((0 - sum([int(x.split(' ')[-1]) for x in data if x.startswith("up")])) + \
            sum([int(x.split(' ')[-1]) for x in data if x.startswith("down")]))
    
    print(total)


def part_2(data: List[str]) -> None:
    # Must be using Python 3.1x for this to work.
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

    print(pos*depth)


if __name__ == "__main__":
    filepath = Path(__file__).parent / "day_02_input.txt"
    data = filepath.read_text().split("\n")
    part_1(data)
    part_2(data)
