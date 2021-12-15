from itertools import chain
from pathlib import Path
from typing import Dict, List, Tuple


def part_2(data: List[str]) -> None:
    total = 0

    for line in data:
        patterns, output = line.split('|')
        patterns = [''.join(sorted(x)) for x in patterns.strip().split(' ')]
        output = [''.join(sorted(x)) for x in output.strip().split(' ')]

        digits_map = {(6, 3, 3): '0',
                      (2, 2, 2): '1',
                      (5, 2, 2): '2',
                      (5, 3, 3): '3',
                      (4, 4, 2): '4',
                      (5, 3, 2): '5',
                      (6, 3, 2): '6',
                      (3, 2, 3): '7',
                      (7, 4, 3): '8',
                      (6, 4, 3): '9'} # type: Dict[Tuple[int, int, int], str]
        
        _4 = ''
        _7 = '' 
        for p in patterns:
            match len(p):
                case 4:
                    _4 = p
                case 3:
                    _7 = p

        readout = []
        for digit in output:
            num_wires = len(digit)
            d = set(digit)
            includes_4 = len(list(d.intersection(_4)))
            includes_7 = len(list(d.intersection(_7)))
            readout.append(digits_map.get((num_wires, includes_4, includes_7), ''))
                    
        total += int(''.join(readout))
    print(total)


def part_1(data: chain) -> None:
    print(len([x for x in data if len(x) in (2, 3, 4, 7,)])) # segments for digits 1, 7, 4, and 8


if __name__ == "__main__":
    filepath = Path(__file__).parent / "day_08_input.txt"
    full_data = filepath.read_text().splitlines()
    readout_data = chain(*[y.split('|')[-1].lstrip().split(' ') for y in full_data])
    part_1(readout_data)
    part_2(full_data)
