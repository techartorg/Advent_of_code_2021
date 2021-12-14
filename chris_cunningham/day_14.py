from collections import Counter


def main():
    with open("inputs/day_14.txt", 'r') as f:
        template, rules = parse_inputs(f.read())

    print(f"Part One: {solve(template, rules, 10)}")
    print(f"Part Two: {solve(template, rules, 40)}")


def parse_inputs(inputs: str) -> tuple[str, dict[str, tuple[str, ...]]]:
    template, rules = inputs.split("\n\n")
    rules = {c[0]: (c[0][0] + c[1], c[1] + c[0][1]) for i in rules.splitlines() if (c := i.split(" -> "))}
    return template, rules


def solve(template: str, rules: dict[str, tuple[str, ...]], steps: int) -> int:
    pair_counts: Counter[str] = Counter(template[i] + item for i, item in enumerate(template[1:]))

    for _ in range(steps):
        temp: Counter[str] = Counter()

        for pair, count in pair_counts.items():
            temp += {m: count for m in rules[pair]}

        pair_counts = temp

    char_counts = Counter()

    for pair, count in pair_counts.items():
        char_counts[pair[0]] += count

    char_counts[template[-1]] += 1

    max_, *_, min_ = char_counts.most_common()
    return max_[1] - min_[1]


if __name__ == '__main__':
    main()
