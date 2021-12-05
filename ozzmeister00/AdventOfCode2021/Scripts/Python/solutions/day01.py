"""
Python day01
"""

from utils.solver import ProblemSolver
import utils.math


class Day01Solver(ProblemSolver):
    def __init__(self):
        super(Day01Solver, self).__init__(1)

        self.testDataPartOne = {'''199
200
208
210
200
207
240
269
260
263''': 7}
        self.testDataPartTwo = {'''199
200
208
210
200
207
240
269
260
263''': 5}

    def ProcessInput(self, data=None):
        """
        Takes the input test string and turns the strings into integers

        :param string data:
        :returns list[int]: processed data for today's challenge
        """
        if not data:
            data = self.rawData

        # turn each new line into integers, if there's valid data in the line
        processed = [int(i) for i in data.split('\n') if i.strip()]

        return processed

    def SolvePartOne(self, data=None):
        """
        Count the number of times the sonar depth reading increases
        by figuring out the delta between the current reading and the next
        and saturating the value

        :param list data: list of depth readings

        :returns int: The solution to today's challenge
        """
        if not data:
            data = self.processed

        countIncreases = 0
        currDepth = data[0]

        # start at the second reading, since the first reading means NoChange
        for i, depth in enumerate(data[1:]):
            # find the delta between the submarine's current depth and the sonar reading ahead
            delta = depth - currDepth

            # clamp the delta between 0 and 1 and add that result to the increases
            countIncreases += int(utils.math.saturate(delta))

            # then set the current depth for the next test
            currDepth = depth

        return countIncreases

    def SolvePartTwo(self, data=None):
        """
        
        :param data:
        :returns: The solution to part two of today's challenge
        """
        if not data:
            data = self.processed

        windows = []

        # build a list of 3-reading sums
        for i in range(0, len(data)-2):
            windows.append(sum(data[i:i+3]))

        return self.SolvePartOne(windows)


if __name__ == '__main__':
    day01 = Day01Solver()
    day01.Run()
