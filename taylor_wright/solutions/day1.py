"""
Day 1 Solution
"""
from itertools import pairwise
from solutions.helpers import rolling_window


def get_depth_measurements():
    return [int(depth) for depth in open('inputs/day1.txt', 'r').read().splitlines()]


def get_part_01_answer(iterable):
    return sum([prev < cur for prev, cur in pairwise(iterable)])


def get_part_02_answer():
    return get_part_01_answer([sum(window) for window in rolling_window(get_depth_measurements(), 3)])


print("Part 01 Answer: {}".format(get_part_01_answer(get_depth_measurements())))
print("Part 02 Answer: {}".format(get_part_02_answer()))
