from pathlib import Path
from typing import List


def part_2(data: List[int]) -> None:
    fuel_rates = [ ]
    current_fuel_rate = 0    
    for a in range(max(data)):
        for b in data:
            dist = abs(b - a)
            rate = 0
            for i in range(dist):
                rate += i + 1
            
            current_fuel_rate += rate

        fuel_rates.append(current_fuel_rate)
        current_fuel_rate = 0
    
    print(min(fuel_rates))


def part_1(data: List[int]) -> None:
    fuel_rates = [ ]
    current_fuel_rate = 0    
    for a in range(max(data)):
        for b in data:
            current_fuel_rate += abs(b - a)

        fuel_rates.append(current_fuel_rate)
        current_fuel_rate = 0
    
    print(min(fuel_rates))


if __name__ == "__main__":
    filepath = Path(__file__).parent / "day_07_input.txt"
    data = ([int(x) for x in filepath.read_text().split(',')])
    part_1(data)
    part_2(data)
