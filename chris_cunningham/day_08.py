count_to_digit = {
    2: 1,
    4: 4,
    3: 7,
    7: 8,
}

Input = tuple[list[str], list[str]]


def main():
    with open("inputs/day_08.txt", 'r') as f:
        inputs = [parse_line(i) for i in f.read().splitlines()]

    print(f"Part One: {part_one(inputs)}")
    print(f"Part Two: {part_two(inputs)}")


def parse_line(line: str) -> tuple[list[str], list[str]]:
    signals, output = [i.split() for i in line.split(" | ", maxsplit=2)]
    return ["".join(sorted(i)) for i in signals], ["".join(sorted(i)) for i in output]


def part_one(inputs: list[Input]) -> int:
    count = 0
    for _, output in inputs:
        count += sum(any(len(digit) == i for i in count_to_digit.keys()) for digit in output)
    return count


def numbers_from_signals(signals: list[str]) -> dict[int, str]:
    numbers = {}
    others = []

    for i in signals:
        match count := len(i):
            case 2 | 4 | 3 | 7: numbers[count_to_digit[count]] = i
            case _: others.append(i)

    def intersect(x) -> tuple[int, int, int, str]:
        four = len(set(x).intersection(numbers[4]))
        seven = len(set(x).intersection(numbers[7]))
        return len(x), four, seven, x

    for pattern in (intersect(i) for i in others):
        match pattern:
            case 6, 3, 3, num: numbers[0] = num
            case 5, 2, 2, num: numbers[2] = num
            case 5, 3, 3, num: numbers[3] = num
            case 5, 3, 2, num: numbers[5] = num
            case 6, 3, 2, num: numbers[6] = num
            case 6, 4, 3, num: numbers[9] = num

    return numbers


def part_two(inputs: list[Input]) -> int:
    total_output = 0

    for signals, output in inputs:
        mappings = {v: str(k) for k, v in numbers_from_signals(signals).items()}
        output_number = "".join(mappings[i] for i in output)
        total_output += int(output_number)

    return total_output


if __name__ == '__main__':
    main()
