
puzzle_input = open(__file__.replace('.py', '_input.txt')).read()

test_input = r'''5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
'''

test_input_2 = r'''11111
19991
19191
19991
11111
'''

from collections import defaultdict


class Grid:
    def __init__(self, input_):
        self.grid = self.populate_grid(input_)
        self.spent = []
        self.flashes = 0
    
    def populate_grid(self, input_):
        lines = input_.splitlines()
        self.height = len(lines)
        self.width = len(lines[0].strip())

        grid = {}
        for y, l in enumerate(lines):
            for x, v in enumerate(l):
                grid[(x,y)] = int(v)
        return grid

    def update_energy_level(self, position):

        if position in self.spent:
            return
        
        self.grid[position] += 1
        if self.grid[position] > 9:

            self.spent.append(position)
            self.flashes += 1
            self.update_neighbors(position)

    def update_neighbors(self, position):

        x, y = position
        for x1 in range(-1, 2):
            for y1 in range(-1, 2):

                if x1 == 0 and y1 == 0:
                    continue
                try:
                    self.grid[(x+x1, y+y1)]
                except KeyError:
                    pass
                else:
                    self.update_energy_level((x+x1, y+y1))
    
    def update_grid(self):
        for position, value in self.grid.items():
            if value > 9:
                self.grid[position] = 0
        
    
    def run(self):
        for position in self.grid.keys():
            self.update_energy_level(position)
        
    
    def simulate(self, steps):
        for i in range(steps):
            try:
                self.run()
                self.update_grid()
                self.spent = []

                if sum(self.grid.values()) == 0:
                    print(f'Flash Detected {i}')
            except RuntimeError:
                pass

        print(f'Number of flashes: {self.flashes}')
    
    def __repr__(self):
        rows = []
        for y in range(self.height):
            r = ''
            for x in range(self.width):
                r += str(self.grid[(x, y)])
            rows.append(r)
        return '\n'.join(rows)



def part_one(input_):
    g = Grid(input_)
    g.simulate(100)
    return g.flashes

assert part_one(test_input) == 1656
print(part_one(puzzle_input))