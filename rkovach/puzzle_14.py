from collections import defaultdict


puzzle_input = open(__file__.replace('.py', '_input.txt')).read()

test_input = r'''NNCB

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
CN -> C
'''

def parse_input(input_):
    template = None
    rules = {}
    for l in input_.splitlines():
        if l and '->' not in l:
            template = l
        elif '->' in l:
            pair, element = l.split(' -> ')
            rules[pair] = element
    return template, rules


# Part One, Brute force string replacement...
def part_one(input_):

    template, rules = parse_input(input_)

    def update_polymer(polymer):
        new = ''
        insertions = []
        for i in range(len(polymer)):
            pair = polymer[i:i+2]
            if len(pair) != 2:
                continue
            insertions.append(rules[pair])
        for i, e1 in enumerate(polymer):
            new += e1
            try:
                new += insertions[i]
            except:
                pass
        return new
    
    polymer = template

    for i in range(10):
        polymer = update_polymer(polymer)
    
    def score(polymer):
        elements = list(set(polymer))
        occurances = {}
        for e in elements:
            occurances[e] = polymer.count(e)
        min_ = min(occurances.values())
        max_ = max(occurances.values())
        return max_ - min_
    
    return score(polymer)


# Part Two, counting with dictionaries...
def part_two(input_):

    pair_count = defaultdict(int)

    template, rules = parse_input(input_)
    splits = {}
    for pair, elem in rules.items():
        a = pair[0] + elem
        b = elem + pair[1]
        splits[pair] = [a, b]
        pair_count[pair] = 0

    elements = list(set(rules.values()))
    polymers = {x : 0 for x in elements}

    steps = 40

    pairs = [template[i:i+2] for i in range(len(template) - 1)]
    for x in set(pairs):
        pair_count[x] += pairs.count(x)

    for i in range(steps):
        tmp = defaultdict(int)
        for p, cnt in pair_count.items():
            a, b = splits[p]
            tmp[a] += cnt
            tmp[b] += cnt
            tmp[p] -= cnt

        for k, v in tmp.items():
            pair_count[k] += v
 
    for p, cnt in pair_count.items():
        polymers[p[0]] += cnt
    polymers[template[-1]] += 1

    min_ = min(polymers.values())
    max_ = max(polymers.values())
    return max_ - min_


assert part_one(test_input) == 1588
print(f'Part One: {part_one(puzzle_input)}')


assert part_two(test_input) == 2188189693529
print(f'Part Two: {part_two(puzzle_input)}')
