"""
Day 2 Solution
"""


def get_movements():
    return [coord for coord in open('inputs/day2.txt', 'r').read().splitlines()]


def get_part_01_answer(movements):
    depth, pos = 0, 0
    for movement in movements:
        match movement.split():
            case ('forward', mag):
                pos += int(mag)
            case ('down', mag):
                depth += int(mag)
            case ('up', mag):
                depth -= int(mag)
            case _:
                print('Invalid Movement')

    return depth * pos


def get_part_02_answer(movements):
    depth, pos, aim = 0, 0, 0
    for movement in movements:
        match movement.split():
            case ('forward', mag):
                pos += int(mag)
                depth += aim * int(mag)
            case ('down', mag):
                aim += int(mag)
            case ('up', mag):
                aim -= int(mag)
            case _:
                print('Invalid Movement')

    return depth * pos


print("Part 01 Answer: {}".format(get_part_01_answer(get_movements())))
print("Part 02 Answer: {}".format(get_part_02_answer(get_movements())))
