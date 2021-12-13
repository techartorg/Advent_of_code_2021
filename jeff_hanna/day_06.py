from collections import Counter
from copy import copy
from pathlib import Path


def calc_fish_lives(fish: Counter, days:int)-> None:
    new_fish = Counter()
    for _x in range(days):
        new_fish.clear()
        for f, count in fish.items():
            if f == 0:
                new_fish[6] += count
                new_fish[8] += count
            else:
                new_fish[f - 1] += count
            
        fish = copy(new_fish)
        
    print(fish.total()) # type:ignore
            

if __name__ == "__main__":
    filepath = Path(__file__).parent / "day_06_input.txt"
    data = Counter([int(x) for x in filepath.read_text().split(',')])
    calc_fish_lives(data, 80)
    calc_fish_lives(data, 256)