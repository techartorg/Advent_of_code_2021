def main():
    inputs = [int(i) for i in open("inputs/day_01.txt", 'r').readlines()]

    part_one = sum(inputs[i + 1] > x for i, x in enumerate(inputs[:-1]))
    print(f"Part One: {part_one}")

    windows = [sum(inputs[i:i + 3]) for i, _ in enumerate(inputs)]
    part_two = sum(windows[i + 1] > x for i, x in enumerate(windows[:-1]))
    print(f"Part two: {part_two}")


if __name__ == '__main__':
    main()

