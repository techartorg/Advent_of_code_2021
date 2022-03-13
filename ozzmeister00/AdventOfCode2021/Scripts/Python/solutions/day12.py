"""
Python day12
"""

import collections
import string

from utils.solver import ProblemSolver


class Cave(object):
    Small = 0
    Large = 1

    def __init__(self, caveID=None, size=Small):
        self._id = caveID
        self.size = size
        self.connections = []

    @property
    def ID(self):
        return self._id

    @ID.setter
    def ID(self, value):
        self._id = value
        self.size = int(self._id[0] in string.ascii_uppercase)

    def addConnection(self, caveID):
        """
        Register a new connection from this cave to somewhere else

        :param str caveID: The ID of the cave to which this cave connects
        """
        if caveID not in self.connections:
            self.connections.append(caveID)

    def __repr__(self):
        return 'Cave(caveID={}, size={})'.format(self.ID, self.size)


class Path(list):
    def __init__(self, *args, **kwargs):
        super(Path, self).__init__(*args, **kwargs)

    def canVisit(self, cave, revisitCave):
        """
        Returns true if this path can visit the input cave

        :param Cave cave: the cave to test
        :param str revisitCave: the id of the cave we're allowed to revisit

        :return bool: if this path can visit the input cave
        """
        # if the cave is small, chelf a couple other things
        if cave.size == Cave.Small:
            # if we haven't visited the cave, return True
            if cave.ID not in self:
                return True
            # otherwise, if the cave we're trying to visit is the revisit cave
            # AND we haven't already visited it
            elif cave.ID == revisitCave and self.count(cave.ID) == 1:
                return True
        # if the cave is big, then we can return to it
        else:
            return True

    def moveTo(self, location):
        """
        Create a new path, moving the the input location
        :param str location: the cave ID of the cave we're moving to
        :return Path: a new path, at the input location
        """

        newSelf = Path(self)
        newSelf.append(location)
        return newSelf

    def isTerminal(self):
        """
        :returns bool: If this path has reached the end
        """
        return self[-1] == 'end'

    def __str__(self):
        return ','.join(self)


class day12Solver(ProblemSolver):
    def __init__(self):
        super(day12Solver, self).__init__(12)

        self.testDataPartOne = {'''start-A
start-b
A-c
A-b
b-d
A-end
b-end''': 10,
                                '''dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc''':19,
                                '''fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW''':226}
        self.testDataPartTwo = {list(self.testDataPartOne.keys())[0]: 36,
                                list(self.testDataPartOne.keys())[1]: 103,
                                list(self.testDataPartOne.keys())[2]: 3509}

    def ProcessInput(self, data=None):
        """
        
        :param data:
        :returns: processed data for today's challenge
        """
        if not data:
            data = self.rawData

        processed = collections.defaultdict(Cave)
        for line in data.split('\n'):
            beginning, end = line.split('-')
            processed[beginning].addConnection(end)
            processed[end].addConnection(beginning)

        # make sure the caves update their ID, since we created them with a default dict
        for caveID in processed:
            processed[caveID].ID = caveID

        return processed

    def solvePaths(self, data, revisit=None):
        """
        Loop through all the possible paths to find
        the set of terminal paths that exist in the data set
        without revisiting any small caves

        :param dict{str: Cave}: the cave system to parse
        :param str revisit: the cave which can be revisited in this solver

        :return list[Path]: all the paths generated by solving the input cave system
        """
        start = Path(['start'])
        paths = [start]
        terminalPaths = []

        # while we still have paths to search
        while len(paths) > 0:
            newPaths = []
            for i, path in enumerate(paths):
                location = path[-1]
                # if the path has arrived at the end, move it over to the list of terminal paths
                if path.isTerminal():
                    # when a path is found to be terminal, convert it to a string so it can be hashed later
                    terminalPaths.append(str(path))
                # otherwise, create new paths for each valid connection
                # in the connections from our current location
                else:
                    for connection in data[location].connections:
                        # if the connection meets criteria
                        if path.canVisit(data[connection], revisit):
                            newPaths.append(path.moveTo(connection))

            paths = newPaths  # move our new paths over to the paths variable

        return terminalPaths

    def SolvePartOne(self, data=None):
        """
        
        :param data:
        :returns: The solution to today's challenge
        """
        if not data:
            data = self.processed

        terminalPaths = self.solvePaths(data)

        return len(terminalPaths)

    def SolvePartTwo(self, data=None):
        """
        
        :param data:
        :returns: The solution to part two of today's challenge
        """
        if not data:
            data = self.processed

        paths = set(self.solvePaths(data))
        # for each small cave (excluding start and end), solve the paths if that
        # cave is the one we can revisit
        smallCaves = [k for k in list(data.keys()) if k[0] in string.ascii_lowercase and k != 'start' and k != 'end']
        for cave in smallCaves:
            newPaths = set(self.solvePaths(data, revisit=cave))
            # union the sets together, because that's faster than comparing lists
            paths = paths.union(newPaths)

        return len(paths)


if __name__ == '__main__':
    day12 = day12Solver()
    day12.Run()