"""
Python day13
"""

from utils.solver import ProblemSolver
from utils.math import Grid2D, Int2

testData = '''6,10
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
fold along x=5'''

class day13Solver(ProblemSolver):
    def __init__(self):
        super(day13Solver, self).__init__(13)

        self.testDataPartOne = {testData: 17}
        self.testDataPartTwo = {}

    def ProcessInput(self, data=None):
        """
        
        :param data:
        :returns: processed data for today's challenge
        """
        if not data:
            data = self.rawData

        lines = data.split('\n')
        splitPoint = lines.index('\n')
        coords = lines[:splitPoint]
        instructions = lines[splitPoint:]

        processed = None

        return processed

    def SolvePartOne(self, data=None):
        """
        
        :param data:
        :returns: The solution to today's challenge
        """
        if not data:
            data = self.processed

    def SolvePartTwo(self, data=None):
        """
        
        :param data:
        :returns: The solution to part two of today's challenge
        """
        if not data:
            data = self.processed


if __name__ == '__main__':
    day13 = day13Solver()
    day13.Run()
