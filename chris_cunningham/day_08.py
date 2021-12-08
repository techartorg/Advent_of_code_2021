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
    _0_6_9 = []
    _2_3_5 = []

    for i in signals:
        match count := len(i):
            case 5:
                _2_3_5.append(i)
            case 6:
                _0_6_9.append(i)
            case _:
                numbers[count_to_digit[count]] = i

    for i in _0_6_9:
        num = set(i)
        if len(num.intersection(numbers[1])) == 1:
            numbers[6] = i
        elif len(num.intersection(numbers[4])) == 4:
            numbers[9] = i
        else:
            numbers[0] = i

    for i in _2_3_5:
        num = set(i)
        if len(num.intersection(numbers[1])) == 2:
            numbers[3] = i
        elif len(num.intersection(numbers[6])) == 5:
            numbers[5] = i
        else:
            numbers[2] = i

    assert len(numbers) == 10
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
