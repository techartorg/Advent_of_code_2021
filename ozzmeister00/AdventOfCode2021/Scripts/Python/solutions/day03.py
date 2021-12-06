"""
Python day03.py
"""

from utils.solver import ProblemSolver


class day03Solver(ProblemSolver):
    def __init__(self):
        super(day03Solver, self).__init__(3)

        self.testDataPartOne = {"""00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010""": 198}
        self.testDataPartTwo = {}

    def ProcessInput(self, data=None):
        """
        
        :param string data: the raw list of binary integers
        :returns list[[bool]]: convert the binary values to a list of bools
        """
        if not data:
            data = self.rawData

        processed = [[bool(int(j)) for j in i] for i in data.split('\n')]

        return processed

    def findCommonBit(self, position, data, matchedValue=True):
        """
        :param int position: the position in the data for which to
        find the most common bit
        :param list[[bool]] data: the data on which to find the most common bit
        :param bool matchedValue: the value to return if the number of 1s and the number of 0s at
        the input position is equal

        :return bool: the most common bit at that position
        """
        positionValues = [i[position] for i in data]
        trueCount = positionValues.count(True)
        falseCount = positionValues.count(False)
        if trueCount > falseCount:
            return True
        elif trueCount == falseCount:
            return matchedValue
        else:
            return False

    def SolvePartOne(self, data=None):
        """
        
        :param data:
        :returns: The solution to today's challenge
        """
        if not data:
            data = self.processed

        # for each position in the bit
        commonBit = []
        for y in range(len(data[0])):
            commonBit.append(self.findCommonBit(y, data))

        # there's probably a better way to do this
        gammaRate = int(''.join(['1' if i else '0' for i in commonBit]), 2)
        episolonRate = int(''.join(['0' if i else '1' for i in commonBit]), 2)

        return gammaRate * episolonRate

    def SolvePartTwo(self, data=None):
        """
        filter bits by their given critera and produce a list of the bit values
        matching criteria for each required diagnostic

        :param list[[bool]] data: list of bitarrays from the diagnostic report
        :returns int: the life support rating as determined by the diagnostic report
        """
        if not data:
            data = self.processed

        oxygenValues = []
        scrubberValues = []

if __name__ == '__main__':
    day03 = day03Solver()
    day03.Run()
