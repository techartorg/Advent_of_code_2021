from contextlib import suppress
from pathlib import Path
from typing import List


def calc_number_of_increases(data: List[int]) -> int:
    num_increases = 0
    for i, x in enumerate(data):
        with suppress(IndexError):
            if data[i + 1] > x:
                num_increases += 1

    return num_increases


def calc_number_of_triplet_increases(data: List[int]) -> int:
    
    num_increases = 0
    #for i in range(0, len(data), 2):
    for i in range(len(data)):
        first_triplet = 0
        second_triplet = 0
        with suppress(IndexError):
            for j in range(i, i+3):
                first_triplet += data[j]
            
            for j in range(i+1, i+4):
                second_triplet += data[j]

            if second_triplet > first_triplet:
                num_increases += 1

    return num_increases



if __name__ == "__main__":
    filepath = Path(__file__).parent / "day_01_input.txt"
    data = [int(x) for x in filepath.read_text().split("\n")]
    result = calc_number_of_increases(data)
    print(f"The number of increases in the data is: {result}.")

    result = calc_number_of_triplet_increases(data)
    print(f"The number of increases in the triplets in the data is: {result}.")
