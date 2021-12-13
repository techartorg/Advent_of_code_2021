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
        self.testDataPartTwo = {list(self.testDataPartOne.keys())[0]: 230}

    def ProcessInput(self, data=None):
        """
        
        :param string data: the raw list of binary integers
        :returns list[[bool]]: convert the binary values to a list of bools
        """
        if not data:
            data = self.rawData

        processed = [[bool(int(j)) for j in i] for i in data.split('\n')]

        return processed

    def findCommonBit(self, position, data, matchedValue=1):
        """
        :param int position: the position in the data for which to
        find the most common bit
        :param list[[bool]] data: the data on which to find the most common bit
        :param int matchedValue: the value to return if the number of 1s and the number of 0s at
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

    def filterValues(self, position, inList, common=True):
        """

        :param int position: the bit position to test
        :param list inList: list of byte values
        :param bool common: to check the most, or least common value

        :return list: list of bytes that match the input criteria
        """
        # if we've reached the end of the list, or if the size of the filtered list is 1
        # return the list
        if position == len(inList[0]) or len(inList) == 1:
            return inList

        # find the common bit at the given position
        commonBit = self.findCommonBit(position, inList, matchedValue=-1)

        # if we're looking for the least common value, flip the bool
        if not common and commonBit != -1:
            commonBit = not commonBit
        # if however, there were equal number of bits, use the one passed in instead
        elif commonBit == -1:
            commonBit = common

        # then create a new list from the input list of bytes with
        # the specified bit in the search position
        outList = [i for i in inList if i[position] == commonBit]

        # increment the search position
        position += 1

        # and filter the list anew
        return self.filterValues(position, outList, common=common)

    def bitArrayToString(self, inList):
        """
        :param list[bool] inList: the list of boolean values to convert

        :return int: the value as expressed as a decimal
        """
        binString = ''.join(['1' if i else '0' for i in inList])

        return binString

    def binStringToDecimal(self, inString):
        """
        Convert a string of 0s and 1s to decimal

        :param str inString: string to convert

        :return int: the input value expressed as a decimal integer
        """

        return int(inString, 2)

    def SolvePartTwo(self, data=None):
        """
        filter bits by their given critera and produce a list of the bit values
        matching criteria for each required diagnostic

        :param list[[bool]] data: list of bitarrays from the diagnostic report
        :returns int: the life support rating as determined by the diagnostic report
        """
        if not data:
            data = self.processed

        oxygenValues = self.filterValues(0, data, common=True) # find the most common values
        scrubberValues = self.filterValues(0, data, common=False)  # find the least common values

        oxygenValue = self.bitArrayToString(oxygenValues[0])
        scrubberValue = self.bitArrayToString(scrubberValues[0])

        return self.binStringToDecimal(oxygenValue) * self.binStringToDecimal(scrubberValue)


if __name__ == '__main__':
    day03 = day03Solver()
    day03.Run()
