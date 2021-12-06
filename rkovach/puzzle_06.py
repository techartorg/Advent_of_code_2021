from collections import defaultdict

test_input = r'''3,4,3,1,2'''
puzzle_input = open(__file__.replace('.py', '_input.txt')).read()


# Part One - The Naive Approached worked ok, but did not work for Part Two...
class Fish:
    def __init__(self, timer=None):
        if timer:
            self.timer = timer
        else:
            self.timer = 9
    
    def evaluate(self):
        countdown = self.timer - 1
        if countdown < 0:
            self.timer = 6
            return [Fish()]
        else:
            self.timer = countdown
        return []


def parse_input(input_):
    initial_population = []
    for x in input_.split(','):
        initial_population.append(Fish(timer=int(x)))
    return initial_population


def run(initial_population, length):
    day = 1
    end = length
    fish_population = list(initial_population)
    while day <= end:
        for f in fish_population:
            fish_population.extend(f.evaluate())
        day += 1

    return len(fish_population)


# Part Two - Having fun with dictionaries...
def part2(input_, days):
    fish_pop = defaultdict(int)
    for i in range(10):
        fish_pop[i] = 0
    
    for x in input_.split(','):
        fish_pop[int(x)] += 1
    

    for i in range(1, days+1):
        for timer, count in fish_pop.items():
            if count > 0:
                newtimer = timer - 1
                if newtimer < 0:
                    fish_pop[9] += 1 * count
                    fish_pop[7] += 1 * count
                    fish_pop[0] -= 1 * count
                else:
                    fish_pop[timer] -= 1 * count
                    fish_pop[newtimer] += 1 * count
    
    return get_population_count(fish_pop)


def get_population_count(pop_dict):
    return sum(v for v in pop_dict.values())



assert (run(parse_input(test_input), 18)) == 26
assert (run(parse_input(test_input), 80)) == 5934

assert (part2(test_input, 18)) == 26
assert (part2(test_input, 256)) == 26984457539

print(f'Part One (slow): {run(parse_input(puzzle_input), 80)}')
print(f'Part One: {part2(puzzle_input, 80)}')
print(f'Part Two: {part2(puzzle_input, 256)}')
