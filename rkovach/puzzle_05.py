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

from collections import defaultdict, namedtuple
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

Point = namedtuple('Point', 'x y')

class Line:
    def __init__(self, start_position, end_position):
        self.p1 = start_position
        self.p2 = end_position
    
    @property
    def x_length(self):
        return self.p2.x - self.p1.x
    
    @property
    def y_length(self):
        return self.p2.y - self.p1.y
    
    @property
    def is_diagonal(self):
        return abs(self.p2.x - self.p1.x) == abs(self.p2.y - self.p1.y)


def parse_input(input_):
    """Convert the puzzle input in a list of "Line" objects."""
    lines = []
    for l in input_.splitlines():
        tokens = l.split('->')
        startpos, endpos = tokens[0], tokens[1]

        startpos = startpos.split(',')
        x1 = int(startpos[0])
        y1 = int(startpos[1])
        p1 = Point(x1, y1)

        endpos = endpos.split(',')
        x2 = int(endpos[0])
        y2 = int(endpos[1])
        p2 = Point(x2, y2)

        line = Line(p1, p2)
        lines.append(line)

    return lines


def solve(lines):
    part1_points = defaultdict(int)
    part2_points = defaultdict(int)

    for line in lines:
        p1, p2 = line.p1, line.p2
        # Only consider Lines which are Horizonal or Vertical.
        # We can find out if they are by comparing the distance between
        # the points on each axis.
        if line.x_length == 0:
            start, end = sorted((p1.y, p2.y))
            for i in range(start, end+1):
                part1_points[(p1.x, i)] += 1

        elif line.y_length == 0:
            start, end = sorted((p1.x, p2.x))
            for i in range(start, end+1):
                part1_points[(i, p1.y)] += 1
        
        # Part two
        if line.is_diagonal:
            # Need to determine which way the line travels so we can find
            # all the points in between.
            x_offset = copysign(1, line.x_length)
            y_offest = copysign(1, line.y_length)

            x = p1.x
            y = p1.y
            # From the starting point, step once diagonally until we reach
            # the end point.
            while True:
                part2_points[(x, y)] += 1
                if (x, y) == (p2.x, p2.y):
                    break
                x += x_offset
                y += y_offest
    
    counter1 = sum(v > 1 for v in part1_points.values())

    # add the results of part 1 to part 2.
    for k, v in part1_points.items():
        part2_points[k] += v
    counter2 = sum(v > 1 for v in part2_points.values())

    return(counter1, counter2)


lines = parse_input(test_input)

test_results = solve(lines)
assert test_results[0] == 5
assert test_results[1] == 12

lines = parse_input(puzzle_input)

puzzle_results = solve(lines)
print(f'Part One: {puzzle_results[0]}')
print(f'Part Two: {puzzle_results[1]}')
