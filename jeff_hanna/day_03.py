from collections import Counter
from pathlib import Path
from typing import List, Optional


def part_1(data: List[str]) -> None:
    gamma_rate = ""
    epsilon_rate = ""
    c = Counter()

    for i in range(len(data[0])):
        c.clear()
        c.update([x[i] for x in data])
        common_vals = c.most_common()
        gamma_rate += common_vals[0][0]
        epsilon_rate += common_vals[-1][0]

    print(int(gamma_rate, 2) * int(epsilon_rate, 2))


def _find_rating( data: List[str], target_val: str, start_bit: int) -> str:
    c = Counter([x[start_bit] for x in data])
    idx = 0 if target_val == "1" else -1
    significant_bit = ""
    if len(c.values()) == 1:
        significant_bit = str(c[0]) # type: ignore
    elif list(c.values())[0] == list(c.values())[-1]:
        significant_bit = target_val
    else:
        significant_bit = c.most_common()[idx][0]

    matched_data = []
    for x in data:
        if x[start_bit] == significant_bit:
            matched_data.append(x)

    if len(matched_data) == 1:
        return matched_data[0]
    else:
        val = _find_rating(matched_data, target_val, start_bit + 1)
        if val:
            return val

    return ""


def part_2(data: List[str]) -> None:
    o2_rating = int(_find_rating(data, "1", 0), 2)
    co2_rating = int(_find_rating(data, "0", 0), 2)
    print(o2_rating * co2_rating)


if __name__ == "__main__":
    filepath = Path(__file__).parent / "day_03_input.txt"
    data = filepath.read_text().splitlines()
    part_1(data)
    part_2(data)
