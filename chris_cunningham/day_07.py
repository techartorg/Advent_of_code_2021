from statistics import mean, median


def main():
    with open("inputs/day_07.txt", 'r') as f:
        inputs = [int(i) for i in f.read().split(",")]
        # print("".join(chr(i) for i in inputs))  # wish it was

    part_one, part_two = solve(inputs)
    print(f"Part One: {part_one}")
    print(f"Part Two: {part_two}")


def solve(inputs: list[int]) -> tuple[int, int]:
    median_dist = int(median(inputs))
    mean_dist = int(mean(inputs))

    part_one = 0
    candidates = [0] * 3

    for value in inputs:
        part_one += int(abs(value - median_dist))
        for index, mod in enumerate(range(-1, 2)):
            candidates[index] += sum(n for n in range(1, abs(value - mean_dist + mod) + 1))

    return part_one, min(candidates)


if __name__ == '__main__':
    main()
