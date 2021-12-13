r'''
--- Day 9: Smoke Basin ---
These caves seem to be lava tubes. Parts are even still volcanically active; 
small hydrothermal vents release smoke into the caves that slowly settles like 
rain.

If you can model how the smoke flows through the caves, you might be able to 
avoid it and be that much safer. The submarine generates a heightmap of the 
floor of the nearby caves for you (your puzzle input).

Smoke flows to the lowest point of the area it's in. For example, consider 
the following heightmap:

    2199943210
    3987894921
    9856789892
    8767896789
    9899965678

Each number corresponds to the height of a particular location, where 9 is the 
highest and 0 is the lowest a location can be.

Your first goal is to find the low points - the locations that are lower than 
any of its adjacent locations. Most locations have four adjacent locations 
(up, down, left, and right); locations on the edge or corner of the map have 
three or two adjacent locations, respectively. (Diagonal locations do not count 
as adjacent.)

In the above example, there are four low points, all highlighted: two are in 
the first row (a 1 and a 0), one is in the third row (a 5), and one is in the 
bottom row (also a 5). All other locations on the heightmap have some lower 
adjacent location, and so are not low points.

The risk level of a low point is 1 plus its height. In the above example, the 
risk levels of the low points are 2, 1, 6, and 6. The sum of the risk levels of 
all low points in the heightmap is therefore 15.

Find all of the low points on your heightmap. What is the sum of the risk levels 
of all low points on your heightmap?


--- Part Two ---
Next, you need to find the largest basins so you know what areas are most 
important to avoid.

A basin is all locations that eventually flow downward to a single low point. 
Therefore, every low point has a basin, although some basins are very small. 
Locations of height 9 do not count as being in any basin, and all other 
locations will always be part of exactly one basin.

The size of a basin is the number of locations within the basin, including the 
low point. The example above has four basins.

The top-left basin, size 3:

    2199943210
    3987894921
    9856789892
    8767896789
    9899965678

The top-right basin, size 9:

    2199943210
    3987894921
    9856789892
    8767896789
    9899965678

The middle basin, size 14:

    2199943210
    3987894921
    9856789892
    8767896789
    9899965678

The bottom-right basin, size 9:

    2199943210
    3987894921
    9856789892
    8767896789
    9899965678

Find the three largest basins and multiply their sizes together. In the above 
example, this is 9 * 14 * 9 = 1134.

What do you get if you multiply together the sizes of the three largest basins?

'''

test_input = r'''2199943210
3987894921
9856789892
8767896789
9899965678
'''

puzzle_input = open(__file__.replace('.py', '_input.txt')).read()


class Grid:
    def __init__(self, input_):
        self.positions = {}
        for y, l in enumerate(input_.splitlines()):
            for x, depth in enumerate([int(d) for d in l]):
                self.positions[(x, y)] = depth
    
    def get_neighbors(self, coord):
        neighbors = []
        for offset in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            new_coord = (coord[0] + offset[0], coord[1] + offset[1])
            try:
                neighbor = self.positions[new_coord]
            except KeyError:
                pass
            else:
                neighbors.append(new_coord)
        return neighbors

    def get_low_points(self):
        low_points = []
        for coord, depth in self.positions.items():
            lowpoint = True

            neighbors = self.get_neighbors(coord)
            for neighbor in neighbors:
                if self.positions[neighbor] <= depth:
                    lowpoint = False
                    break

            if lowpoint:
               low_points.append(coord)

        return(low_points)

    def expand_basin(self, coord):
        basin_locations = [coord]
        neighbor_count = len(self.get_neighbors(coord))
        while neighbor_count != 0:
            for c in basin_locations:
                neighbors = self.get_neighbors(c)
                neighbor_count = 0
                for n in neighbors:
                    if n in basin_locations:
                        continue
                    elif self.positions[n] == 9:
                        continue
                    else:
                        neighbor_count += 1
                        basin_locations.append(n)

        return basin_locations


def part_one(input_):
    grid = Grid(input_)
    low_points = grid.get_low_points()
    answer = 0
    for p in low_points:
        answer += grid.positions[p] + 1
    return answer


def part_two(input_):
    grid = Grid(input_)
    low_points = grid.get_low_points()

    basin_sizes = []
    for p in low_points:
        basin = grid.expand_basin(p)
        basin_sizes.append(len(basin))
    
    basin_sizes = sorted(basin_sizes)

    return basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3]


assert part_one(test_input) == 15
assert part_two(test_input) == 1134

print(f'Part One: {part_one(puzzle_input)}')
print(f'Part Two: {part_two(puzzle_input)}')
