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


''' Not working efficiently...
def part_two():
    memo = {}
    template, rules = parse_input(puzzle_input)
    memo2 = {}

    for polymer, element in rules.items():
        memo[polymer] = polymer[0] + element + polymer[1]
    
    def run(polymer):
        i = 0
        for e in polymer:
            pair = polymer[i:i+2]
            if len(pair) != 2:
                continue
            polymer = polymer.replace(pair, memo[pair], 1)
            i += 2
        return polymer

    for k in rules.keys():
        polymer = k
        for i in range(10):
            polymer = run(polymer)
        memo2[k] = polymer
    
    initial_pairs = []
    for i, e in enumerate(template):
        pair = template[i:i+2]
        if len(pair) != 2:
            continue
        initial_pairs.append(pair)
    
    polymer = ''
    for p in initial_pairs:
        polymer += memo2[p]
    
    def score(polymer):
        elements = list(set(polymer))
        occurances = {}
        for e in elements:
            occurances[e] = polymer.count(e)

        min_ = min(occurances.values())
        max_ = max(occurances.values())
        return max_ - min_

    print(score(polymer))

'''

assert part_one(test_input) == 1588
print(f'Part One: {part_one(puzzle_input)}')
