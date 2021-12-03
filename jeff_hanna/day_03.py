from collections import Counter
from pathlib import Path
from typing import List


def part_1(data: List[str]) -> None:
    gamma_rate = ""
    epsilon_rate = ""

    for i in range(len(data[0])):
        c = Counter([x[i] for x in data])
        gamma_rate += c.most_common()[0][0]
        epsilon_rate += c.most_common()[-1][0]

    print(int(gamma_rate, 2) * int(epsilon_rate, 2))


if __name__ == "__main__":
    filepath = Path(__file__).parent / "day_03_input.txt"
    data = filepath.read_text().splitlines()
    part_1(data)