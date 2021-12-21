"""
Python day04
"""

from utils.helpers import Grid2D
from utils.solver import ProblemSolver


class BingoBoard(Grid2D):
    def __init__(self, inString):
        rows = inString.split('\n')
        columns =



class day04Solver(ProblemSolver):
    def __init__(self):
        super(day04Solver, self).__init__(4)

        self.testDataPartOne = {"""7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7""": 4512}
        self.testDataPartTwo = {}

    def ProcessInput(self, data=None):
        """
        
        :param data:
        :returns: processed data for today's challenge
        """
        if not data:
            data = self.rawData

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
    day04 = day04Solver()
    day04.Run()
