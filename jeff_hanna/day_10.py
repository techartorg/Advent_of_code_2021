from pathlib import Path
from typing import List

_PAIRS = ("()", "[]", "{}", "<>")
_CLOSERS = {'(': ')', '[': ']', '{': '}', '<': '>'}
_P1_SCORING_TABLE = {')': 3, ']': 57, '}': 1197, '>': 25137}
_P2_SCORING_TABLE = {')': 1, ']': 2, '}': 3, '>': 4}

def _eliminate_pairs(line: str) -> str:
    line_in = line
    for x in _PAIRS:
        line_in = line_in.replace(x, '')

    if line == line_in:
        return line_in

    return(_eliminate_pairs(line_in))


def part_1(data:List[str]) -> None:
    score = 0
    
    for d in data:
        trimmed_line = _eliminate_pairs(d)
        corrupted_elements = {trimmed_line.index(x):x for x in _CLOSERS.values() if x in trimmed_line}
        if corrupted_elements:
            closer = corrupted_elements.get(min(corrupted_elements.keys()), '')
            if not closer:
                continue
            score += _P1_SCORING_TABLE.get(closer, 0)
        
    print(score)


def part_2(data:List[str]) -> None:
    scores = []
    
    for d in data:
        score = 0
        trimmed_line = _eliminate_pairs(d)
        corrupted_elements = {trimmed_line.index(x):x for x in _CLOSERS.values() if x in trimmed_line}
        if not corrupted_elements:
            ordered_openers = list(trimmed_line)
            ordered_openers.reverse()
            for c in ''.join([_CLOSERS.get( x, '') for x in ordered_openers]):
                score *= 5
                score += _P2_SCORING_TABLE.get(c, 0)
            
            scores.append(score)


    print(sorted(scores)[len(scores)//2])


if __name__ == "__main__":
    filepath = Path(__file__).parent / "day_10_input.txt"
    data = filepath.read_text().splitlines()
    part_1(data)
    part_2(data)
