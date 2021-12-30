"""
05
"""
import math

from utils.processing import commaSeparatedIntegers
from utils.math import Int2, Float2, Grid2D
from utils.solver import ProblemSolver


class Grid2DLineAccumulator(Grid2D):
    """
    A specialized Grid2D class for accumulating lines onto a grid of integers
    """
    def __init__(self, width, height, **kwargs):
        super(Grid2DLineAccumulator, self).__init__(width, data=[0 for i in range(width * height)])

    def drawLine(self, start, end, ortho=False):
        """
        Adds 1 to the coordinates covered by a given line

        :param Int2 start: where the line starts
        :param Int2 end: where the line ends
        :param bool ortho: if true, only support orthogonal lines
        """
        if start.x == end.x:
            self.drawColumn(start.x, start.y, end.y)
        elif start.y == end.y:
            self.drawRow(start.y, start.x, end.x)
        elif not ortho:
            # try some Bresenham via Wikipedia, but this is giving negative values for the line pointers
            linePointer = Float2(start)
            dx = abs(end.x - start.x)
            sx = 1 if start.x < end.x else -1
            dy = -abs(end.y - start.y)
            sy = 1 if start.x < end.x else -1
            err = dx + dy

            visitedPoints = []

            while linePointer != end:
                point = Int2(linePointer)
                visitedPoints.append(point)  # append the rounded point to the list of visited points
                print(point)
                self[point] += 1

                e2 = 2 * err
                if e2 >= dy:
                    err += dy
                    linePointer.x += sx
                if e2 <= dx:
                    err += dx
                    linePointer.y += sy

                print(self)  # debug

            for point in list(set(visitedPoints)):
                print(point)
                self[point] += 1

    def drawRow(self, row, start, end):
        if start > end:
            start, end = end, start
        for x in range(start, end+1):
            self[Int2((x, row))] += 1

    def drawColumn(self, column, start, end):
        if start > end:
            start, end = end, start

        for y in range(start, end+1):
            self[Int2((column, y))] += 1

    def countAbove(self, value):
        """
        Get the count of values in the array above an input value

        :param int value: the value to test
        """
        return len([1 for i in self if i > value])


class DaySolver05(ProblemSolver):
    def __init__(self):
        super(DaySolver05, self).__init__(5)

        self.testDataPartOne = {'''0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2''':5}
        self.testDataPartTwo = {list(self.testDataPartOne.keys())[0]:12}

    def ProcessInput(self, data=None):
        """
        :param str data: the input list of line coordinates

        :returns int, int, list[(Int2, Int2)]: width, height, and list of start/end coordinates
        """
        if not data:
            data = self.rawData

        processed = []
        width = 0
        height = 0

        for line in data.split('\n'):
            # convert both sides of the input string to Int2s since they're both comma-separated int arrays
            processed.append([Int2(commaSeparatedIntegers(i)) for i in line.split(' -> ')])

            # bump out the width and height based on the input lines
            # so that we know how big of a grid to make later
            for point in processed[-1]:
                width = max(point.x, width)
                height = max(point.y, height)

        return width+1, height+1, processed

    def SolvePartOne(self, data=None, ortho=True):
        """
        :param list[int, int, list[(Int2, Int2)] data: the width, height, and lines (defined by start and end points)
        :param bool ortho: if true, test only orthogonal lines
        
        :return : the result
        """
        if not data:
            data = self.processed

        # unpack the input data
        width, height, lines = data

        grid = Grid2DLineAccumulator(width, height)
        for start, end in lines:
            grid.drawLine(start, end, ortho=ortho)

        print(grid)

        return grid.countAbove(1)

    def SolvePartTwo(self, data=None):
        """
        :param list[int, int, list[(Int2, Int2)] data: the width, height, and lines (defined by start and end points)
        
        :return : the result
        """
        return self.SolvePartOne(data=data, ortho=False)


def Main():
    solver = DaySolver05()
    solver.TestAlgorithm(solver.SolvePartTwo, part=2)


if __name__ == '__main__':
    Main()
