test_input = r'''2199943210
3987894921
9856789892
8767896789
9899965678
'''

puzzle_input = open(__file__.replace('.py', '_input.txt')).read()


class Point:
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.is_peak = value == 9
        self.is_lowpoint = False
        self.value = value
    
    def __repr__(self):
        return f'Point ({self.x}, {self.y} has a depth of {self.value}.)'


class Grid:
    def __init__(self, input_):
        self.positions = {}
        for y, l in enumerate(input_.splitlines()):
            for x, depth in enumerate([int(d) for d in l]):
                self.positions[(x, y)] = Point(x, y, depth)
    
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


def part_one(input_):
    grid = Grid(input_)
    low_points = get_low_points(grid)
    answer = 0
    for p in low_points:
        answer += grid.positions[p].value + 1
    return answer


def part_two(input_):
    grid = Grid(input_)
    low_points = get_low_points(grid)

    basin_sizes = []
    for p in low_points:
        basin = expand_basin(grid, p)
        basin_sizes.append(len(basin))
    
    basin_sizes = sorted(basin_sizes)

    return basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3]


def get_low_points(grid):
    low_points = []
    for coord, point in grid.positions.items():
        lowpoint = True

        neighbors = grid.get_neighbors(coord)
        for neighbor in neighbors:
            if grid.positions[neighbor].value <= point.value:
                lowpoint = False
                break

        point.is_lowpoint = lowpoint
        if lowpoint:
           low_points.append(coord)

    return(low_points)


def expand_basin(grid, coord):
    basin_locations = [coord]
    neighbor_count = len(grid.get_neighbors(coord))
    while neighbor_count != 0:
        for c in basin_locations:
            neighbors = grid.get_neighbors(c)
            neighbor_count = 0
            for n in neighbors:
                if n in basin_locations:
                    continue
                elif grid.positions[n].is_peak:
                    continue
                else:
                    neighbor_count += 1
                    basin_locations.append(n)

    return basin_locations


assert part_one(test_input) == 15
assert part_two(test_input) == 1134

print(f'Part One: {part_one(puzzle_input)}')
print(f'Part Two: {part_two(puzzle_input)}')
