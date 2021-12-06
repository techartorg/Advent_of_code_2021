from collections import defaultdict

fish = [int(v) for v in open("day_06_input.txt").read().split(",")]
# I should probably use the smarter solution for both parts, but at least for now I'm going to keep both the slow and fast versions.

fish_one = fish[:]
for i in range(80):
    new = [v - 1 if v != 0 else 6 for v in fish_one]
    new.extend([8] * fish_one.count(0))
    fish_one[:] = new

print(len(fish_one))
# Basically just grouping the fish instead of tracking each individually
fish_age_counter: defaultdict[int, int] = defaultdict(int)
for f in fish:
    fish_age_counter[f] += 1

for i in range(256):
    new_ages: defaultdict[int, int] = defaultdict(int)
    for age, count in fish_age_counter.items():
        if age:
            new_ages[age - 1] += count
        else:
            new_ages[6] += count
            new_ages[8] += count
    fish_age_counter = new_ages

print(sum(fish_age_counter.values()))
