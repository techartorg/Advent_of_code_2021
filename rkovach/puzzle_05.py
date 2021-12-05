r'''--- Day 5: Hydrothermal Venture ---
You come across a field of hydrothermal vents on the ocean floor! These vents 
constantly produce large, opaque clouds, so it would be best to avoid them if 
possible.

They tend to form in lines; the submarine helpfully produces a list of nearby 
lines of vents (your puzzle input) for you to review. For example:

    0,9 -> 5,9
    8,0 -> 0,8
    9,4 -> 3,4
    2,2 -> 2,1
    7,0 -> 7,4
    6,4 -> 2,0
    0,9 -> 2,9
    3,4 -> 1,4
    0,0 -> 8,8
    5,5 -> 8,2

Each line of vents is given as a line segment in the format x1,y1 -> x2,y2 
where x1,y1 are the coordinates of one end the line segment and x2,y2 are the 
coordinates of the other end. These line segments include the points at both 
ends. In other words:

    - An entry like 1,1 -> 1,3 covers points 1,1, 1,2, and 1,3.
    - An entry like 9,7 -> 7,7 covers points 9,7, 8,7, and 7,7.

For now, only consider horizontal and vertical lines: lines where either 
x1 = x2 or y1 = y2.

So, the horizontal and vertical lines from the above list would produce the 
following diagram:

    .......1..
    ..1....1..
    ..1....1..
    .......1..
    .112111211
    ..........
    ..........
    ..........
    ..........
    222111....

In this diagram, the top left corner is 0,0 and the bottom right corner is 9,9. 
Each position is shown as the number of lines which cover that point or . if no 
line covers that point. The top-left pair of 1s, for example, comes from 
2,2 -> 2,1; the very bottom row is formed by the overlapping lines 0,9 -> 5,9 
and 0,9 -> 2,9.

To avoid the most dangerous areas, you need to determine the number of points 
where at least two lines overlap. In the above example, this is anywhere in 
the diagram with a 2 or larger - a total of 5 points.

Consider only horizontal and vertical lines. At how many points do at least 
two lines overlap?


--- Part Two ---
Unfortunately, considering only horizontal and vertical lines doesn't give you 
the full picture; you need to also consider diagonal lines.

Because of the limits of the hydrothermal vent mapping system, the lines in 
your list will only ever be horizontal, vertical, or a diagonal line at exactly 
45 degrees. In other words:

    - An entry like 1,1 -> 3,3 covers points 1,1, 2,2, and 3,3.
    - An entry like 9,7 -> 7,9 covers points 9,7, 8,8, and 7,9.

Considering all lines from the above example would now produce the following 
diagram:

    1.1....11.
    .111...2..
    ..2.1.111.
    ...1.2.2..
    .112313211
    ...1.2....
    ..1...1...
    .1.....1..
    1.......1.
    222111....

You still need to determine the number of points where at least two lines 
overlap. In the above example, this is still anywhere in the diagram with a 
2 or larger - now a total of 12 points.

Consider all of the lines. At how many points do at least two lines overlap?

'''

from collections import defaultdict
from math import copysign


puzzle_input = open(__file__.replace('.py', '_input.txt')).read()

test_input = r'''0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
'''

def parse_input(input_):

    part1_points = defaultdict(int)
    part2_points = defaultdict(int)

    lines = []
    for l in input_.splitlines():
        tokens = l.split()
        startpos, endpos = tokens[0], tokens[-1]

        startpos = startpos.split(',')
        startpos_x = int(startpos[0])
        startpos_y = int(startpos[-1])

        endpos = endpos.split(',')
        endpos_x = int(endpos[0])
        endpos_y = int(endpos[-1])

        # For horizonal and vertical lines we can just find the low point
        # and step through the in between positions.
        # diagonal lines in part two are little trickier.
        if startpos_x == endpos_x:
            start_y = min(startpos_y, endpos_y)
            end_y = max(startpos_y, endpos_y)
            for i in range(start_y, end_y + 1):
                part1_points[(startpos_x, i)] += 1
                part2_points[(startpos_x, i)] += 1

        elif startpos_y == endpos_y:
            start_x = min(startpos_x, endpos_x)
            end_x = max(startpos_x, endpos_x)
            for i in range(start_x, end_x + 1):
                part1_points[(i, startpos_y)] += 1
                part2_points[(i, startpos_y)] += 1
        
        # Part two
        if abs(endpos_x - startpos_x) == abs(endpos_y - startpos_y):

            # need to determine which way the line travels.
            x_len = endpos_x - startpos_x
            y_len = endpos_y - startpos_y

            x_offset = copysign(1, x_len)
            y_offest = copysign(1, y_len)

            x = startpos_x
            y = startpos_y
            # from the starting point, step once diagonally until we reach
            # the end point.
            while True:
                part2_points[(x, y)] += 1
                if (x, y) == (endpos_x, endpos_y):
                    break
                x += x_offset
                y += y_offest
    
    counter1 = 0
    for pos, value in part1_points.items():
        if value > 1:
            counter1 += 1

    counter2 = 0
    for pos, value in part2_points.items():
        if value > 1:
            counter2 += 1

    return(counter1, counter2)


test_results = parse_input(test_input)
assert test_results[0] == 5
assert test_results[1] == 12

puzzle_results = parse_input(puzzle_input)
print(f'Part One: {puzzle_results[0]}')
print(f'Part Two: {puzzle_results[1]}')
