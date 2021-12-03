dir_map = {
    "forward": 1,
    "down": 1j,
    "up": -1j,
}


def parse(inst: str) -> complex:
    d, s = inst.split(" ", maxsplit=2)
    return dir_map[d] * int(s)


def part_one(inputs: list[complex]) -> int:
    summed = sum(inputs)
    return int(summed.real * summed.imag)


def part_two(inputs: list[complex]) -> int:
    pos = 0+0j
    aim = 0

    for i in inputs:
        aim += i.imag
        pos += complex(real=i.real, imag=aim * i.real)

    return int(pos.real * pos.imag)


def main():
    inputs = [parse(i) for i in open("inputs/day_02.txt", 'r').readlines()]
    print(f"Part One: {part_one(inputs)}")
    print(f"Part Two: {part_two(inputs)}")


if __name__ == '__main__':
    main()
