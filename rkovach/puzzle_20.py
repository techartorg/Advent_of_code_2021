test_input = r'''..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

#..#.
#....
##..#
..#..
..###
'''

puzzle_input = open(__file__.replace('.py', '_input.txt')).read()

import copy
from collections import defaultdict
from operator import itemgetter
import time

class Image:

    def __init__(self, input_):
        self.parse_input(input_)
        self.step = 0
    
    def parse_input(self, input_):
        lines = input_.splitlines()
        self.key = lines[0]
        self.initialize_image(self.key[0], lines[2:])

    def initialize_image(self, default, input_):
        # This part is tricky, and the key to the whole thing... when accessing
        # pixels outside the known extents, those pixels are turning on and
        # off each step, and will influence the values along the border of the 
        # known pixels.
        if default == '#':
            pixels = defaultdict(lambda:self.step % 2)
        else:
            pixels = defaultdict(lambda:0)

        # Convert the "#" and "." to 0s and 1s so we can count the pixels
        # easier at the end.
        for row, line in enumerate(input_):
            for column, pixel in enumerate(line):
                pixels[(column,row)] = 1 if pixel == '#' else 0

        self.image = pixels
        self.get_image_dimensions()
    
    def get_image_dimensions(self):
        # since this only gets called once, and we start at 0,0 - this could
        # be simplified.
        coords = list(self.image.keys())

        self.min_x = min(coords, key=itemgetter(0))[0]
        self.max_x = max(coords, key=itemgetter(0))[0]
        self.min_y = min(coords, key=itemgetter(1))[1]
        self.max_y = max(coords, key=itemgetter(1))[1]

    def enhance_image(self):
        # iterate through the image, but we also need to consider each
        # pixel just outside the current image. expand the range of pixel
        # coordinates by 1 in each direction to get the border pixels.
        enhanced_image = copy.copy(self.image)
        for x in range(self.min_x - 1, self.max_x + 2):
            for y in range(self.min_y - 1, self.max_y + 2):
                enhanced_image[(x, y)] = self.get_enhanced_pixel(x, y)
        self.image = enhanced_image

        # expand the range for the next step.
        self.min_x -= 1
        self.max_x += 1
        self.min_y -= 1
        self.max_y += 1

        self.step += 1
    
    def get_enhanced_pixel(self, x, y):
        # get the 8 neighbors of the current pixel, convert the values into
        # a nine-digit binary string and convert to an integer to look up the
        # new value from the "key". Neighrbors are read left-to-right, top-to-
        # bottom.
        binary = ''
        for y1 in range(-1,2):
            for x1 in range(-1,2):
                binary += str(self.image[(x + x1, y + y1)])
        offset = int(binary, 2)
        new_pixel = self.key[offset]
        return 1 if new_pixel == '#' else 0

    def __repr__(self):
        # print the current image for debugging.
        rows = []
        for y in range(self.min_y, self.max_y + 1):
            r = ''
            for x in range(self.min_x, self.max_x + 1):
                r += '#' if self.image[(x, y)] == 1 else '.'
            rows.append(r)
        print('\n'.join(rows).count('#'))
        return '\n'.join(rows)




def part_one(input_):
    t0 = time.time()

    im = Image(input_)
    for i in range(2):
        im.enhance_image()

    print(time.time() - t0)
    return sum(im.image.values())

def part_two(input_):
    t0 = time.time()

    im = Image(input_)
    for i in range(50):
        im.enhance_image()

    print(time.time() - t0)
    return sum(im.image.values())

assert part_one(test_input) == 35
assert part_two(test_input) == 3351

print(f'Part One: {part_one(puzzle_input)}.')
print(f'Part Two: {part_two(puzzle_input)}.')