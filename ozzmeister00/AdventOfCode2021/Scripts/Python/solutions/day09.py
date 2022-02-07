"""
--- Day 9: Smoke Basin ---
These caves seem to be lava tubes. Parts are even still volcanically active;
 small hydrothermal vents release smoke into the caves that slowly settles like rain.

If you can model how the smoke flows through the caves, you might be able to
avoid it and be that much safer. The submarine generates a heightmap of the
floor of the nearby caves for you (your puzzle input).

Smoke flows to the lowest point of the area it's in. For example,
consider the following heightmap:

2199943210
3987894921
9856789892
8767896789
9899965678
Each number corresponds to the height of a particular location,
where 9 is the highest and 0 is the lowest a location can be.

Your first goal is to find the low points - the locations that are lower than any of its adjacent locations.
 Most locations have four adjacent locations (up, down, left, and right); locations on the edge or
 corner of the map have three or two adjacent locations, respectively. (Diagonal locations do not count as adjacent.)

In the above example, there are four low points, all highlighted: two are in the first row (a 1 and a 0),
 one is in the third row (a 5), and one is in the bottom row (also a 5). All other locations on the heightmap
  have some lower adjacent location, and so are not low points.

The risk level of a low point is 1 plus its height. In the above example, the risk levels of the low points are
2, 1, 6, and 6. The sum of the risk levels of all low points in the heightmap is therefore 15.

Find all of the low points on your heightmap. What is the sum of the risk levels of all low points on your heightmap?

To begin, get your puzzle input.
"""
import math

from utils.solver import ProblemSolver
from utils.math import Grid2D, Int2


class day09Solver(ProblemSolver):
    def __init__(self):
        super(day09Solver, self).__init__(9)

        self.testDataPartOne = {'''2199943210
3987894921
9856789892
8767896789
9899965678''': 15}
        self.testDataPartTwo = {'''2199943210
3987894921
9856789892
8767896789
9899965678''':1134}

    def ProcessInput(self, data=None):
        """
        
        :param data:
        :returns: processed data for today's challenge
        """
        if not data:
            data = self.rawData

        lines = data.replace('\n', '')
        width = len(data.split('\n')[0])

        integers = [int(i) for i in lines]

        processed = Grid2D(width=width, data=integers)

        return processed

    def identifyLowPoints(self, data):
        """
        :params Grid2D data: the grid of height values for which to find the low points
        :returns list[Int2]: the coordinates of the low points in the grid
        """
        lowPoints = []
        for i, value in enumerate(data):
            coords = data.indexToCoords(i)
            higherValues = []
            localNeighbors = list(data.enumerateOrthoLocalNeighbors(coords))
            for neighbor, neighborValue in localNeighbors:
                if neighborValue > value:
                    higherValues.append(neighborValue)

            # if the number of higher points around this one are equal to the number of local neighbors
            if len(higherValues) == len(localNeighbors):
                # then add this coordinate to the low points list, because everyone around us is too tall
                lowPoints.append(coords)

        return lowPoints

    def SolvePartOne(self, data=None):
        """
        
        :param data:
        :returns: The solution to today's challenge
        """
        if not data:
            data = self.processed

        riskLevel = 0
        lowPoints = self.identifyLowPoints(data)
        for point in lowPoints:
            riskLevel += data[point] + 1

        return riskLevel

    def buildBasin(self, point, basin, data):
        """
        Recurse through the neighbors of a given point, and if any of their values are not 9
        include them in the list of points comprising the basin. Once we reach the edge of the basin, return the basin

        :param Int2 point: the point to test
        :param list basin: the list of points already in the basin
        :param Grid2D data: the heightmap to test

        :returns list: the list of points comprising the basin
        """
        for neighbor, height in data.enumerateOrthoLocalNeighbors(point):
            if neighbor not in basin and height != 9:
                basin.append(neighbor)
                basin = self.buildBasin(neighbor, basin, data)

        return basin

    def SolvePartTwo(self, data=None):
        """
        
        :param data:
        :returns: The solution to part two of today's challenge
        """
        if not data:
            data = self.processed

        # grab all the low points in the input heighmap
        lowPoints = self.identifyLowPoints(data)

        # then seek out from those points to build the basins for each point
        basins = []
        for point in lowPoints:
            basins.append(self.buildBasin(point, [point], data))

        # finally, get the size of all the basins
        basinSizes = [len(basin) for basin in basins]

        # sort those sizes so that
        basinSizes.sort()

        # we can get the product of the size of the three largest basins
        return math.prod(basinSizes[-3:])


if __name__ == '__main__':
    day09 = day09Solver()
    day09.Run()
