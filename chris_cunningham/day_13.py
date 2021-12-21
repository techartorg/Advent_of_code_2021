Pt = tuple[int, int]
Inst = tuple[str, int]


def main():
    with open("inputs/day_13.txt", 'r') as f:
        grid, instructions = parse_inputs(f.read())

    count, code = solve(grid, instructions)
    print(f"Part One: {count}")
    print(f"Part Two:\n{code}")


def parse_inputs(inputs: str) -> tuple[set[Pt], list[Inst]]:
    points_str, instructions_str = inputs.split("\n\n", maxsplit=2)

    grid = set()
    for pt in points_str.splitlines():
        x, y = pt.split(",", maxsplit=2)
        grid.add((int(x), int(y)))

    instructions = []
    for inst in instructions_str.splitlines():
        *_, value = inst.split(" ")
        axis, coord = value.split("=", maxsplit=2)
        instructions.append((axis, int(coord)))

    return grid, instructions


def print_grid(grid: set[Pt]) -> str:
    width = max(x for x, _ in grid) + 1
    height = max(y for _, y in grid) + 1
    return "\n".join("".join("█" if (x, y) in grid else " " for x in range(width)) for y in range(height))


def solve(grid: set[Pt], instructions: list[Inst]) -> tuple[int, str]:
    first_fold_count = 0

    for i, (axis, amount) in enumerate(instructions):
        if axis == "x":
            grid = {(min(x, 2 * amount - x), y) for x, y in grid}
        else:
            grid = {(x, min(y, 2 * amount - y)) for x, y in grid}
        if i == 0:
            first_fold_count = len(grid)

    return first_fold_count, print_grid(grid)


if __name__ == '__main__':
    main()
