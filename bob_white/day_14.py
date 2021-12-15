from collections import Counter

example = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""

start, rules = example.split("\n\n")
# Part 1 can be done pretty naively
start, rules = open("day_14_input.txt").read().split("\n\n")

rule_map: dict[str, str] = {}
for rule in rules.split("\n"):
    p, insert = rule.split(" -> ")
    rule_map[p] = insert
for _ in range(10):
    new = ""
    for i in range(len(start) - 1):
        current = start[i : i + 2]
        new += current[0] + rule_map[current]
    new += start[-1]
    start = new
counts = Counter(start)
print(max(counts.values()) - min(counts.values()))


# Part 2 on the other hand...
start, rules = open("day_14_input.txt").read().split("\n\n")


def get_counts(pair: str, iterations: int, *, _memo: dict[tuple[str, int], Counter[str]] = {}) -> Counter[str]:
    if not iterations:
        return Counter(pair)
    if (pair, iterations) not in _memo:
        c = rule_map[pair]
        count: Counter[str] = Counter()
        a, b = pair
        count += get_counts(a + c, iterations - 1)
        count += get_counts(c + b, iterations - 1)
        _memo[(pair, iterations)] = count
    return _memo[(pair, iterations)]


# the `get_counts` function will double count the interior characters, so we want to start with the first and last character at 1
counts: Counter[str] = Counter(start[0] + start[-1])
for i in range(len(start) - 1):
    counts += get_counts(start[i : i + 2], 40)
# then we can just divide the min/max by 2 to get a final value
print((max(counts.values()) - min(counts.values())) // 2)
