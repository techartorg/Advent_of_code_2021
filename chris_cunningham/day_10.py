from typing import Iterable

rtl_map = {v: k for k, v in ["[]", "{}", "<>", "()"]}


def main():
    with open("inputs/day_10.txt", 'r') as f:
        inputs = [parse_line(i) for i in f.read().splitlines()]

    print(f"Part One: {part_one(i for i in inputs if isinstance(i, str))}")
    print(f"Part Two: {part_two(i for i in inputs if isinstance(i, list))}")


def parse_line(line: str) -> str | list[str] | None:
    stack = []

    for c in line:
        match c:
            case '[' | '{' | '<' | '(':
                stack.append(c)
            case _:
                p = stack.pop()
                if p != rtl_map[c]:
                    return c

    if stack:
        return stack


def part_one(inputs: Iterable[str]) -> int:
    score = 0

    for line in inputs:
        match line:
            case ')': score += 3
            case ']': score += 57
            case '}': score += 1197
            case '>': score += 25137

    return score


def part_two(inputs: Iterable[list[str]]) -> int:
    scores = []

    for line in inputs:
        result = 0

        for c in reversed(line):
            result *= 5
            match c:
                case '(': result += 1
                case '[': result += 2
                case '{': result += 3
                case '<': result += 4
        scores.append(result)

    scores.sort()
    return scores[len(scores) // 2]


if __name__ == '__main__':
    main()
