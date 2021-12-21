r'''
--- Day 13: Transparent Origami ---

You reach another volcanically active part of the cave. It would be nice if 
you could do some kind of thermal imaging so you could tell ahead of time 
which caves are too hot to safely enter.

Fortunately, the submarine seems to be equipped with a thermal camera! When 
you activate it, you are greeted with:

Congratulations on your purchase! To activate this infrared thermal imaging
camera system, please enter the code found on page 1 of the manual.

Apparently, the Elves have never used this feature. To your surprise, you 
manage to find the manual; as you go to open it, page 1 falls out. It's a 
large sheet of transparent paper! The transparent paper is marked with 
random dots and includes instructions on how to fold it up (your puzzle 
input). For example:

    6,10
    0,14
    9,10
    0,3
    10,4
    4,11
    6,0
    6,12
    4,1
    0,13
    10,12
    3,4
    3,0
    8,4
    1,10
    2,14
    8,10
    9,0

    fold along y=7
    fold along x=5

The first section is a list of dots on the transparent paper. 0,0 
represents the top-left coordinate. The first value, x, increases to the 
right. The second value, y, increases downward. So, the coordinate 3,0 is 
to the right of 0,0, and the coordinate 0,7 is below 0,0. The coordinates 
in this example form the following pattern, where # is a dot on the paper 
and . is an empty, unmarked position:

    ...#..#..#.
    ....#......
    ...........
    #..........
    ...#....#.#
    ...........
    ...........
    ...........
    ...........
    ...........
    .#....#.##.
    ....#......
    ......#...#
    #..........
    #.#........

Then, there is a list of fold instructions. Each instruction indicates a 
line on the transparent paper and wants you to fold the paper up (for 
horizontal y=... lines) or left (for vertical x=... lines). In this 
example, the first fold instruction is fold along y=7, which designates the 
line formed by all of the positions where y is 7 (marked here with -):

    ...#..#..#.
    ....#......
    ...........
    #..........
    ...#....#.#
    ...........
    ...........
    -----------
    ...........
    ...........
    .#....#.##.
    ....#......
    ......#...#
    #..........
    #.#........

Because this is a horizontal line, fold the bottom half up. Some of the 
dots might end up overlapping after the fold is complete, but dots will 
never appear exactly on a fold line. The result of doing this fold looks 
like this:

    #.##..#..#.
    #...#......
    ......#...#
    #...#......
    .#.#..#.###
    ...........
    ...........

Now, only 17 dots are visible.

Notice, for example, the two dots in the bottom left corner before the 
transparent paper is folded; after the fold is complete, those dots appear 
in the top left corner (at 0,0 and 0,1). Because the paper is transparent, 
the dot just below them in the result (at 0,3) remains visible, as it can 
be seen through the transparent paper.

Also notice that some dots can end up overlapping; in this case, the dots 
merge together and become a single dot.

The second fold instruction is fold along x=5, which indicates this line:

    #.##.|#..#.
    #...#|.....
    .....|#...#
    #...#|.....
    .#.#.|#.###
    .....|.....
    .....|.....

Because this is a vertical line, fold left:

    #####
    #...#
    #...#
    #...#
    #####
    .....
    .....

The instructions made a square!

The transparent paper is pretty big, so for now, focus on just completing 
the first fold. After the first fold in the example above, 17 dots are 
visible - dots that end up overlapping after the fold is completed count as 
a single dot.

How many dots are visible after completing just the first fold instruction 
on your transparent paper?


--- Part Two ---

Finish folding the transparent paper according to the instructions. The 
manual says the code is always eight capital letters.

What code do you use to activate the infrared thermal imaging camera 
system?

'''


test_input = r'''6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
'''

puzzle_input = open(__file__.replace('.py', '_input.txt')).read()

import copy
from collections import defaultdict

def parse_input(input_):
    dots = []
    folds = []
    for l in input_.splitlines():
        try:
            x, y = l.split(',')
            dots.append((int(x), int(y)))
        except:
            if '=' in l:
                tokens = l.split()
                axis, location = tokens[-1].split('=')
                folds.append((axis, int(location)))
    return (dots, folds)

def part_one(input_):
    dots, folds = parse_input(input_)
    grid = defaultdict(int)
    for x in dots:
        grid[x] = 1
    
    grid1 = copy.copy(grid)

    def fold(axis, location):
        for x, y in grid.keys():
            if axis == 'y':
                if y > location:
                    offset = y - location
                    y1 = y - (offset * 2)
                    value = grid1[(x, y1)]
                    grid1[(x, y1)] = min(1, value + 1)
                    grid1[(x, y)] = 0
            elif axis == 'x':
                if x > location:
                    offset = x - location
                    x1 = x - (offset * 2)
                    value = grid1[(x1, y)]
                    grid1[(x1, y)] = min(1, value + 1)
                    grid1[(x, y)] = 0
    
    fold(*folds[0])
    return sum(grid1.values())


def part_two(input_):
    dots, folds = parse_input(input_)
    grid = defaultdict(int)
    for x in dots:
        grid[x] = 1

    def fold(grid, axis, location):
        grid1 = copy.copy(grid)
        for x, y in grid.keys():
            if axis == 'y':
                if y > location:
                    offset = y - location
                    y1 = y - (offset * 2)
                    value = grid1[(x, y1)]
                    grid1[(x, y1)] = min(1, value + 1)
                    grid1.pop((x, y))
            elif axis == 'x':
                if x > location:
                    offset = x - location
                    x1 = x - (offset * 2)
                    value = grid1[(x1, y)]
                    grid1[(x1, y)] = min(1, value + 1)
                    grid1.pop((x, y))
        return grid1
    
    for axis, location in folds:
        grid = fold(grid, axis, location)
    return grid

def print_grid(grid):
    x_values = [x for x, y in grid.keys()]
    y_values = [y for x, y in grid.keys()]

    x_min = min(x_values)
    x_max = max(x_values)
    y_min = min(y_values)
    y_max = max(y_values)

    rows = []
    for y in range(y_min, y_max+1):
        r = ''
        for x in range(x_min, x_max+1):
            r += '#' if grid[(x, y)] > 0 else ' '
        rows.append(r)
    print('\n'.join(rows))


assert part_one(test_input) == 17

print(part_one(puzzle_input))

print_grid(part_two(puzzle_input))



