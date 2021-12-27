"""
04
"""

from utils.math import Grid2D, Int2
from utils.solver import ProblemSolver


class BingoBoard(Grid2D):
    def __init__(self, board):
        """
        :param list[int] board: the bingo board as a list of integers
        """
        super(BingoBoard, self).__init__(5, data=board)
        self.won = False

    def indexToCoords(self, index):
        """
        :param int index: index to convert
        :return
        """
        return Int2((index % self.width, index / self.width))

    def find(self, value):
        """
        :param value: the value to find
        :return Int2: the coordinate of the found item
        """
        return self.indexToCoords(self.index(value))

    def mark(self, value):
        """
        Marks the input value if the value is on the board

        :param int value: the value to mark on the board

        :return bool: if marking this square results in a line
        """
        if value in self:
            coords = self.find(value)
            self[coords] *= -1
            self.won = self.testColumn(coords.x) or self.testRow(coords.y)
            return self.won

        return False

    def gatherRow(self, row):
        """
        :param int row: the row to gather into a list
        """
        return [self[Int2((i, row))] for i in range(5)]

    def gatherColumn(self, column):
        """
        :param int column: the column to gather into a list
        """
        return [self[Int2((column, i))] for i in range(5)]

    def testColumn(self, column):
        """
        :param int column: column to test
        :return bool: if the column is complete
        """
        return self.testComplete(self.gatherColumn(column))

    def testRow(self, row):
        """
        :param int row: the row to test
        :return bool: if the row is complete
        """
        return self.testComplete(self.gatherRow(row))

    def testComplete(self, gathered):
        """
        :param list gathered: the gathered items from a row or column to test
        :return bool: if the row or column is fully marked
        """
        return all([i < 0 for i in gathered])

    def unmarked(self):
        """
        :return list: the unmarked values on the board
        """
        return [i for i in self if i > 0]


class DaySolver04(ProblemSolver):
    def __init__(self):
        super(DaySolver04, self).__init__(4)

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
 2  0 12  3  7""":4512}
        self.testDataPartTwo = {list(self.testDataPartOne.keys())[0]:1924}

    def ProcessInput(self, data=None):
        """
        :param str data:
        """
        if not data:
            data = self.rawData

        callOrder = [int(i) for i in data.split('\n')[0].split(',')]
        processed = []

        rawBoards = data.split('\n')[2:]
        for i in range(0, len(rawBoards), 6):
            boardLines = rawBoards[i:i+5]
            print(boardLines)
            board = ''
            for line in boardLines:
                # clean up accidental double commas because of how the input data is formatted + ','
                board += line.replace(' ', ',') + ','

            board = board[:-1].lstrip(',').replace(',,',',')  # strip off the trailing comma
            print(board)
            board = [int(j) for j in board.split(',')]
            if len(board) != 25:
                raise Exception("Length of a board is not 25: {}".format(board))
            processed.append(BingoBoard(board))

        return callOrder, processed

    def SolvePartOne(self, data=None):
        """
        :param list data: the data to operate on
        
        :return : the result
        """
        if not data:
            data = self.processed

        callOrder, boards = data

        # loop through each call number
        for value in callOrder:
            # then loop over all the boards and mark the value
            for board in boards:
                # if one of the boards won, then return the product of the sum of the unmarked values on the board
                # and the value of the number we just called
                if board.mark(value):
                    return sum(board.unmarked()) * value

        return -1

    def SolvePartTwo(self, data=None):
        """
        :param list data: the data to operate on
        
        :return : the result
        """
        if not data:
            data = self.processed

        callOrder, boards = data
        pointer = 0
        wonBoards = []

        while len(boards) and pointer < len(callOrder):
            popBoards = []

            # iterate over all the boards, and mark the current number
            for i, board in enumerate(boards):
                # if the board won with that mark, add its index to a list to be popped out later
                if board.mark(callOrder[pointer]):
                    popBoards.append(i)

            # after we've figured out all the boards that won with this number, pop them into the wonBoards array
            for pop in popBoards:
                wonBoards.append(boards.pop(pop))

            # increment the pointer
            pointer += 1

        # grab the absolute last board that won, sum its unmarked values, and multiply it by the final called value
        return sum(wonBoards[-1].unmarked()) * callOrder[pointer-1]



def Main():
    solver = DaySolver04()
    solver.Run()


if __name__ == '__main__':
    Main()
