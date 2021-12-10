err_scores = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

valid_points = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}

pairs = ["()", "[]", "{}", "<>"]


def main():
    with open("inputs/day_10.txt", 'r') as f:
        inputs = f.read().splitlines()

    err_score, valid_lines = part_one(inputs)
    print(f"Part One: {err_score}")
    print(f"Part Two: {part_two(valid_lines)}")


def filter_pairs(line: str) -> str:
    filtered = line

    while any(i in filtered for i in pairs):
        for pair in pairs:
            filtered = filtered.replace(pair, "")

    return filtered


def part_one(lines: list[str]) -> tuple[int, list[str]]:
    score = 0
    valid_lines = []

    for line in lines:
        no_pairs = filter_pairs(line)
        errs = sorted((c for _, c in pairs if c in no_pairs), key=lambda x: no_pairs.index(x))
        if errs:
            score += err_scores[errs[0]]
        else:
            valid_lines.append(no_pairs)

    return score, valid_lines


def part_two(lines: list[str]) -> int:
    scores = []
    ltr = {k: v for k, v in pairs}

    for line in lines:
        score = 0
        for c in reversed(line):
            score = score * 5 + valid_points[ltr[c]]
        scores.append(score)

    scores.sort()
    return scores[len(scores) // 2]


if __name__ == '__main__':
    main()
