"""
Python day11
"""

import copy

from utils.math import Grid2D, Int2
from utils.solver import ProblemSolver


class Octopus(object):
    def __init__(self, value):
        super(Octopus, self).__init__()
        self.flashed = False
        self.value = value

    def __add__(self, other):
        # don't add anything to the energy level of this octopus
        # if it has already flashed in this step
        if not self.flashed:
            self.value += other

        # if we exceed, then flash and reset to 0
        if self.value > 9:
            self.flashed = True
            self.value = 0

        return self

    def __str__(self):
        return str(self.value)


class day11Solver(ProblemSolver):
    def __init__(self):
        super(day11Solver, self).__init__(11)

        self.testDataPartOne = {'''5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526''': 1656}
        self.testDataPartTwo = {list(self.testDataPartOne.keys())[0]: 195}

    def ProcessInput(self, data=None):
        """
        
        :param data:
        :returns: processed data for today's challenge
        """
        if not data:
            data = self.rawData

        # grab the width off the dataset
        width = len(data.split('\n')[0])
        # then remove all the newline characters, since Grid2D can handle chunking it up based on width
        data = data.replace('\n', '')

        octopodes = [Octopus(int(i)) for i in data]

        processed = Grid2D(width, data=octopodes)

        return processed

    def cascadeFlash(self, coords, data):
        """
        Increment the neighbors around the input coords recursively
        """
        localFlashes = []
        for neighborCoords, neighbor in data.enumerateNeighborsBox(coords, 1):
            if not neighbor.flashed and neighborCoords != coords:
                data[neighborCoords] += 1
                if data[neighborCoords].flashed:
                    localFlashes.append(neighborCoords)

        for coord in localFlashes:
            data = self.cascadeFlash(coord, data)

        return data

    def stepGrid(self, active):
        """
        Perform a step on the input grid of octopodes

        :param Grid2D active:
        :returns Grid2D:
        """
        # first, step all the octopodes
        flashedCoords = []
        for i, value in enumerate(active):
            active[i] += 1
            if active[i].flashed:
                flashedCoords.append(active.indexToCoords(i))

        # then flash all the coords that initially flashed
        for coord in flashedCoords:
            active = self.cascadeFlash(coord, active)

        return active

    def SolvePartOne(self, data=None):
        """
        
        :param Grid2D data:
        :returns: The solution to today's challenge
        """
        if not data:
            data = self.processed

        active = copy.deepcopy(data)

        steps = 100
        flashes = 0
        while steps:
            active = self.stepGrid(active)

            # then loop over the grid, count the flashes, then reset the flash flag
            for i, value in enumerate(active):
                if active[i].flashed:
                    flashes += 1
                    active[i].flashed = False

            steps -= 1

        return flashes

    def SolvePartTwo(self, data=None):
        """
        
        :param data:
        :returns: The solution to part two of today's challenge
        """
        if not data:
            data = self.processed

        active = copy.deepcopy(data)

        allFlashed = False
        steps = 0
        while not allFlashed:
            active = self.stepGrid(active)

            flashes = 0
            for i, value in enumerate(active):
                if active[i].flashed:
                    flashes += 1
                    active[i].flashed = False

            allFlashed = len(active) == flashes

            steps += 1

        return steps


if __name__ == '__main__':
    day11 = day11Solver()
    day11.Run()
