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
        # store a separate grid for markers
        self.markers = Grid2D(5, data=[False for i in range(25)])
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
            self.markers[coords] = True
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

    def gatherMarkersColumn(self, column):
        """
        :param int column: the column of markers to gather
        """
        return [self.markers[Int2((column, i))] for i in range(5)]

    def gatherMarkersRow(self, row):
        """
        :param int row: the row of markers to gather
        """
        return [self.markers[Int2((i, row))] for i in range(5)]

    def testColumn(self, column):
        """
        :param int column: column to test
        :return bool: if the column is complete
        """
        return self.testComplete(self.gatherMarkersColumn(column))

    def testRow(self, row):
        """
        :param int row: the row to test
        :return bool: if the row is complete
        """
        return self.testComplete(self.gatherMarkersRow(row))

    def testComplete(self, gathered):
        """
        :param list gathered: the gathered items from a row or column to test
        :return bool: if the row or column is fully marked
        """
        return all(gathered)

    def unmarked(self):
        """
        :return list: the unmarked values on the board
        """
        return [self[i] for i, value in enumerate(self.markers) if not value]


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

        # convert the first line of the input data to an array of integers
        callOrder = [int(i) for i in data.split('\n')[0].split(',')]
        processed = []

        # separate out the raw data for board definitions from the call order
        rawBoards = data.split('\n')[2:]
        # loop over each board definition (five lines, followed by a blank, so step the range by 6)
        for i in range(0, len(rawBoards), 6):
            # the board lines are the five lines from the current index forward
            boardLines = rawBoards[i:i+5]
            board = ''
            # for each line in those board lines,
            # replace spaces with commas and add a comma to the end as each one gets added
            for line in boardLines:
                board += line.replace(' ', ',') + ','

            # strip off any leading and trailing commas, as well as collapsing any doublecommas caused by
            # Wastl insisting on using unpadded integers for single-digit values
            board = board[:-1].lstrip(',').replace(',,',',')

            # convert the values in the board to an array of integers
            board = [int(j) for j in board.split(',')]

            # for safety, make sure the board is 25 items long
            if len(board) != 25:
                raise Exception("Length of a board is not 25: {}".format(board))

            # instantiate a bingo board using the array of integers
            processed.append(BingoBoard(board))

        return callOrder, processed

    def SolvePartOne(self, data=None):
        """
        Call numbers in the order determined by our input data and mark boards
        that have that number.

        :param list[list[int], list[BingoBoard]] data: the call numbers in the first index,
                                                       and all the boards that are in play
        
        :return int: the product of the sum of the unmarked numbers on the winning board and the winning called number
        """
        if not data:
            data = self.processed

        # unpack input data
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
        Call numbers in the order determined by our input data and mark boards
        that have that number.

        :param list[list[int], list[BingoBoard]] data: the call numbers in the first index,
                                                       and all the boards that are in play

        :return int: the product of the sum of the unmarked numbers on the last board
                    to win and the number called to seal that win
        """
        if not data:
            data = self.processed

        # unpack input data
        callOrder, boards = data

        # initial setup values
        callPointer = 0
        wonBoards = []

        # while loop testing the number of remaining boards and, for safety, the call pointer
        while len(boards) and callPointer < len(callOrder):
            # iterate over all the boards, and mark the current number
            # use a while loop, since we're popping boards out and for looping and popping aren't friends
            boardPointer = 0
            while boardPointer < len(boards):
                board = boards[boardPointer]
                # if the board won with that mark, pop it over to the wonBoards array
                if board.mark(callOrder[callPointer]):
                    wonBoards.append(boards.pop(boardPointer))
                # otherwise, increment the board pointer and move on to the next board
                else:
                    boardPointer += 1

            # increment the pointer
            callPointer += 1

        # grab the absolute last board that won, sum its unmarked values, and multiply it by the final called value
        return sum(wonBoards[-1].unmarked()) * callOrder[callPointer-1]


def Main():
    solver = DaySolver04()
    solver.Run()


if __name__ == '__main__':
    Main()
