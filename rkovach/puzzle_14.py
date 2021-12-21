r'''
--- Day 14: Extended Polymerization ---
The incredible pressures at this depth are starting to put a strain on your 
submarine. The submarine has polymerization equipment that would produce 
suitable materials to reinforce the submarine, and the nearby volcanically-
active caves should even have the necessary input elements in sufficient 
quantities.

The submarine manual contains instructions for finding the optimal polymer 
formula; specifically, it offers a polymer template and a list of pair 
insertion rules (your puzzle input). You just need to work out what polymer 
would result after repeating the pair insertion process a few times.

For example:

    NNCB

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

The first line is the polymer template - this is the starting point of the 
process.

The following section defines the pair insertion rules. A rule like AB -> C 
means that when elements A and B are immediately adjacent, element C should 
be inserted between them. These insertions all happen simultaneously.

So, starting with the polymer template NNCB, the first step simultaneously 
considers all three pairs:

    - The first pair (NN) matches the rule NN -> C, so element C is inserted 
      between the first N and the second N.
    - The second pair (NC) matches the rule NC -> B, so element B is inserted 
      between the N and the C.
    - The third pair (CB) matches the rule CB -> H, so element H is inserted 
      between the C and the B.

Note that these pairs overlap: the second element of one pair is the first 
element of the next pair. Also, because all pairs are considered simultaneously, 
inserted elements are not considered to be part of a pair until the next step.

After the first step of this process, the polymer becomes NCNBCHB.

Here are the results of a few steps using the above rules:

    Template:     NNCB
    After step 1: NCNBCHB
    After step 2: NBCCNBBBCBHCB
    After step 3: NBBBCNCCNBBNBNBBCHBHHBCHB
    After step 4: NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB

This polymer grows quickly. After step 5, it has length 97; After step 10, it 
has length 3073. After step 10, B occurs 1749 times, C occurs 298 times, H 
occurs 161 times, and N occurs 865 times; taking the quantity of the most 
common element (B, 1749) and subtracting the quantity of the least common 
element (H, 161) produces 1749 - 161 = 1588.

Apply 10 steps of pair insertion to the polymer template and find the most and 
least common elements in the result. What do you get if you take the quantity 
of the most common element and subtract the quantity of the least common 
element?

--- Part Two ---
The resulting polymer isn't nearly strong enough to reinforce the submarine. 
You'll need to run more steps of the pair insertion process; a total of 40 
steps should do it.

In the above example, the most common element is B (occurring 2192039569602 
times) and the least common element is H (occurring 3849876073 times); 
subtracting these produces 2188189693529.

Apply 40 steps of pair insertion to the polymer template and find the most and 
least common elements in the result. What do you get if you take the quantity 
of the most common element and subtract the quantity of the least common 
element?

'''

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
