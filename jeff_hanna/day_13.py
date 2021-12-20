from pathlib import Path


def part_1(data) -> None:
    return


def part_2(data) -> None:
    return


if __name__ == "__main__":
    filepath = Path(__file__).parent / "day_13_input.txt"
    """
    x = [['0,0'], ['0,1'], ['1,-1'], ['1,0']]
    x = tuple([tuple(map(int, elt[0].split(','))) for elt in x])
    """
    raw_data = [x.strip().split('-') for x in filepath.read_text().splitlines() if x]
    part_1(data)
    part_2(data)
