from math import prod


class Tile(object):
    def __init__(self, number: int):
        self.number: int = number
        self.is_hit: bool = False


class Board(object):
    def __init__(self, lines: str):
        self.tiles: dict[tuple[int, int], Tile] = {}
        self.numbers_to_tiles: dict[int, Tile] = {}

        for i, row in enumerate(lines.splitlines()):
            for j, col in enumerate(row.split()):
                position = (j, i)
                number = int(col)
                tile = Tile(number)
                self.tiles[position] = tile
                self.numbers_to_tiles[number] = tile

    def select_number(self, n: int):
        if n in self.numbers_to_tiles:
            self.numbers_to_tiles[n].is_hit = True

    def has_win(self) -> bool:
        row_win = any(all(self.tiles[(row, i)].is_hit for i in range(5)) for row in range(5))
        col_win = any(all(self.tiles[(i, col)].is_hit for i in range(5)) for col in range(5))
        return row_win or col_win

    def get_score(self) -> int:
        score = 0

        for i in range(5):
            for j in range(5):
                if not self.tiles[(i, j)].is_hit:
                    score += self.tiles[(i, j)].number

        return score


def parse_inputs(path: str) -> tuple[list[int], list[Board]]:
    with open(path, 'r') as f:
        sections = f.read().split("\n\n")
        inputs = [int(i) for i in sections[0].split(",")]
        boards = [Board(i) for i in sections[1:]]
        return inputs, boards


def part_one(inputs: list[int], boards: list[Board]) -> int:
    for n in inputs:
        for b in boards:
            b.select_number(n)

            if b.has_win():
                return b.get_score() * n


def part_two(inputs: list[int], boards: list[Board]) -> int:
    last = None
    closed_set = set()

    for n in inputs:
        for b in boards:
            b.select_number(n)

            if b not in closed_set and b.has_win():
                last = (n, b.get_score())
                closed_set.add(b)

    return prod(last)


def main():
    inputs, boards = parse_inputs("inputs/day_04.txt")
    print(f"Part One: {part_one(inputs, boards)}")
    print(f"Part Two: {part_two(inputs, boards)}")


if __name__ == '__main__':
    main()
