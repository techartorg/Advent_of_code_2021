"""
Python day02
"""

from utils.solver import ProblemSolver
import utils.math

class SubmarineDirections:
    """
    Enum class for storing the different commands
    """
    Up = utils.math.Float2([0, -1])
    Down = utils.math.Float2([0, 1])
    Forward = utils.math.Float2([1, 0])

    directionMapping = {"forward": Forward,
                        "down": Down,
                        "up": Up
                        }

    def __init__(self, command):
        self.command = command
        self.direction = SubmarineDirections.directionMapping[command]

    def __repr__(self):
        return "SubmarineDirection('{}')".format(self.command)


class day02Solver(ProblemSolver):
    def __init__(self):
        super(day02Solver, self).__init__(2)

        self.testDataPartOne = {"""forward 5
down 5
forward 8
up 3
down 8
forward 2""": 150}
        self.testDataPartTwo = {list(self.testDataPartOne.keys())[0]: 900}

    def ProcessInput(self, data=None):
        """
        
        :param string data: command list from the puzzle input
        :returns: commands broken down into discrete float2 moves
        """
        if not data:
            data = self.rawData

        processed = []

        for line in data.split('\n'):
            command, value = line.split(' ')
            command = SubmarineDirections(command)
            value = int(value)
            processed.append((command, value))

        return processed

    def SolvePartOne(self, data=None):
        """
        Based on the input list of position changes, compute the
        product of the current depth and forward position.

        :param list[Float2] data:
        :returns int: The submarine's forward position multiplied by its depth
        """
        if not data:
            data = self.processed

        position = utils.math.Float2()
        for command, magnitude in data:
            position = position + (command.direction * magnitude)

        return position.x * position.y

    def SolvePartTwo(self, data=None):
        """
        
        :param data:
        :returns: The solution to part two of today's challenge
        """
        if not data:
            data = self.processed

        position = utils.math.Float2()
        aim = 0

        for command, magnitude in data:
            # if the command is up or down, adjust the aim
            if command.direction != SubmarineDirections.Forward:
                aim += (command.direction.y * magnitude)

            # otherwise, move forward by magnitude and adjust depth
            # by aim * magnitude
            else:
                position.x += magnitude
                position.y += (aim * magnitude)

        return position.x * position.y


if __name__ == '__main__':
    day02 = day02Solver()
    day02.Run()
