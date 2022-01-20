"""
Python day07
"""

from utils.solver import ProblemSolver


class day07Solver(ProblemSolver):
    def __init__(self):
        super(day07Solver, self).__init__(7)

        self.testDataPartOne = {'16,1,2,0,4,2,7,1,2,14':37}
        self.testDataPartTwo = {'16,1,2,0,4,2,7,1,2,14':168}

    def ProcessInput(self, data=None):
        """
        
        :param data:
        :returns: processed data for today's challenge
        """
        if not data:
            data = self.rawData

        return [int(i) for i in data.split(',')]

    def getCrabDistances(self, crabs):
        """
        Return the raw distance between all crabs and one crab in the
        list of all the crab submarines
        """
        distances = []
        maxCrabs = list(sorted(crabs))[-1]
        for position in range(maxCrabs):
            distance = sum([abs(position - crab) for crab in crabs])
            distances.append(distance)

        return distances

    def SolvePartOne(self, data=None):
        """
        
        :param data:
        :returns: The solution to today's challenge
        """
        if not data:
            data = self.processed

        crabs = data.copy()
        distances = self.getCrabDistances(crabs)
        distances.sort()
        return distances[0]

    def SolvePartTwo(self, data=None):
        """
        
        :param data:
        :returns: The solution to part two of today's challenge
        """
        if not data:
            data = self.processed

        maxCrabs = list(sorted(data))[-1]
        fuelCosts = []
        for position in range(maxCrabs):
            fuelCost = sum([sum([x for x in range(abs(position - crab)+1)]) for crab in data])
            fuelCosts.append(fuelCost)

        return list(sorted(fuelCosts))[0]


if __name__ == '__main__':
    day07 = day07Solver()
    day07.Run()
