example = """
[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
"""[
    1:-1
].split(
    "\n"
)
bad_points = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}
good_points = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}

pairs = ["{}", "[]", "()", "<>"]
flipped = {k: v for k, v in pairs}

# This is the real magic, the trick is to remove all matched pairs
# Once completed inner chunks are cleared, we're left with either an incomplete
# or broken line, at which point they can be used either for part 1 or 2
# Luckily the lines are dense enough to hit a recursion error, but I might rewrite this, just in case.
def remove_pairs(line: str) -> str:
    removed = line
    for pair in pairs:
        removed = removed.replace(pair, "")
    if line == removed:
        return removed
    return remove_pairs(removed)


total = 0
good_lines: list[str] = []
for line in open("day_10_input.txt"):
    rl = remove_pairs(line.strip())
    bad = [(c, rl.index(c)) for _, c in pairs if c in rl]
    if bad:
        total += bad_points[min(bad, key=lambda x: x[1])[0]]
    else:
        good_lines.append(rl)

print(total)

good_scores: list[int] = []
for line in good_lines:
    score = 0
    for c in line[::-1]:
        score *= 5
        score += good_points[flipped[c]]
    good_scores.append(score)

good_scores.sort()
print(good_scores[len(good_scores) // 2])
