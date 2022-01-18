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

        return [int(i) for i in data.split(',')]

    def decrement(self, x):
        return x - 1

    def handleDay(self, fish):
        """
        Loops over the input list of fish spawn timers and
        if any are zero, reset them to 6 and add a new fish at 8
        otherwise, decrement the timer
        """
        fish.sort(reverse=True)
        spawningFish = fish.count(0)
        if spawningFish:
            fish = fish[:-spawningFish]

        fish = [i - 1 for i in fish]

        if spawningFish:
            fish += [8, 6] * spawningFish

        return fish

    def SolvePartOne(self, data=None, numDays=80):
        """
        
        :param data:
        :returns: The solution to today's challenge
        """
        if not data:
            data = self.processed

        fish = data.copy()

        start = time.time()

        days = numDays
        while days:
            fish = self.handleDay(fish)
            days -= 1

        end = time.time()
        print(end - start)

        return len(fish)

    def SolvePartTwo(self, data=None):
        """
        
        :param data:
        :returns: The solution to part two of today's challenge
        """
        if not data:
            data = self.processed

        return self.SolvePartOne(numDays=256)


if __name__ == '__main__':
    day06 = day06Solver()
    day06.Run()
