"""
Python day06
"""

import time

from utils.solver import ProblemSolver

decrement = lambda x: x-1

class day06Solver(ProblemSolver):
    def __init__(self):
        super(day06Solver, self).__init__(6)

        self.testDataPartOne = {'3,4,3,1,2': 5934}
        self.testDataPartTwo = {'3,4,3,1,2':26984457539}

    def ProcessInput(self, data=None):
        """
        
        :param data:
        :returns: processed data for today's challenge
        """
        if not data:
            data = self.rawData

        # initialize an array of 9 integers (corresponding to the number of days remaining to spawn
        processed = [0] * 9
        for i in data.split(','):
            processed[int(i)] += 1

        return processed

    def handleDay(self, fish):
        """
        Loops over the input list of fish spawn timers and
        if any are zero, reset them to 6 and add a new fish at 8
        otherwise, decrement the timer
        """
        newFish = fish[0]
        outFish = fish[1:] # slice off the 0 fish, we'll add them back later
        outFish[6] += newFish # add the newFish number of fish to the number of fish waiting 6 days
        # then append the number of new fish to the end of the array,
        # representing the number of fish waiting 8 days to spawn
        outFish.append(newFish)

        return outFish

    def SolvePartOne(self, data=None, numDays=80):
        """
        
        :param data:
        :returns: The solution to today's challenge
        """
        if not data:
            data = self.processed

        fish = data.copy()

        days = numDays
        while days:
            fish = self.handleDay(fish)
            days -= 1

        return sum(fish)

    def SolvePartTwo(self, data=None):
        """
        
        :param data:
        :returns: The solution to part two of today's challenge
        """
        if not data:
            data = self.processed

        return self.SolvePartOne(data=data, numDays=256)


if __name__ == '__main__':
    day06 = day06Solver()
    day06.Run()
