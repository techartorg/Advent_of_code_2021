"""
--- Day 10: Syntax Scoring ---
You ask the submarine to determine the best route out of the deep-sea cave, but it only replies:

Syntax error in navigation subsystem on line: all of them
All of them?! The damage is worse than you thought. You bring up a copy of the navigation subsystem (your puzzle input).

The navigation subsystem syntax is made of several lines containing chunks. There are one or more chunks on each line, and chunks contain zero or more other chunks. Adjacent chunks are not separated by any delimiter; if one chunk stops, the next chunk (if any) can immediately start. Every chunk must open and close with one of four legal pairs of matching characters:

If a chunk opens with (, it must close with ).
If a chunk opens with [, it must close with ].
If a chunk opens with {, it must close with }.
If a chunk opens with <, it must close with >.
So, () is a legal chunk that contains no other chunks, as is []. More complex but valid chunks include ([]), {()()()}, <([{}])>, [<>({}){}[([])<>]], and even (((((((((()))))))))).

Some lines are incomplete, but others are corrupted. Find and discard the corrupted lines first.

A corrupted line is one where a chunk closes with the wrong character - that is, where the characters it opens and closes with do not form one of the four legal pairs listed above.

Examples of corrupted chunks include (], {()()()>, (((()))}, and <([]){()}[{}]). Such a chunk can appear anywhere within a line, and its presence causes the whole line to be considered corrupted.

For example, consider the following navigation subsystem:

[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
Some of the lines aren't corrupted, just incomplete; you can ignore these lines for now. The remaining five lines are corrupted:

{([(<{}[<>[]}>{[]{[(<()> - Expected ], but found } instead.
[[<[([]))<([[{}[[()]]] - Expected ], but found ) instead.
[{[{({}]{}}([{[{{{}}([] - Expected ), but found ] instead.
[<(<(<(<{}))><([]([]() - Expected >, but found ) instead.
<{([([[(<>()){}]>(<<{{ - Expected ], but found > instead.
Stop at the first incorrect closing character on each corrupted line.

Did you know that syntax checkers actually have contests to see who can get the high score for syntax errors in a file? It's true! To calculate the syntax error score for a line, take the first illegal character on the line and look it up in the following table:

): 3 points.
]: 57 points.
}: 1197 points.
>: 25137 points.
In the above example, an illegal ) was found twice (2*3 = 6 points), an illegal ] was found once (57 points), an illegal } was found once (1197 points), and an illegal > was found once (25137 points). So, the total syntax error score for this file is 6+57+1197+25137 = 26397 points!

Find the first illegal character in each corrupted line of the navigation subsystem. What is the total syntax error score for those errors?

To begin, get your puzzle input.
"""

from collections import defaultdict

from utils.solver import ProblemSolver


pointTable = {')': 3,
              ']': 57,
              '}': 1197,
              '>': 25137,
              '(': -3,
              '[': -57,
              '{': -1197,
              '<': -25137
              }

pointTablePart2 = {')':1,
                   ']':2,
                   '}':3,
                   '>':4}


opened = ['(', '[', '{', '<']
closed = [')', ']', '}', '>']

openClose = {opened[i]: closed[i] for i in range(len(opened))}
closeOpen = {closed[i]: opened[i] for i in range(len(opened))}

class day10Solver(ProblemSolver):
    def __init__(self):
        super(day10Solver, self).__init__(10)

        self.testDataPartOne = {'''[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]''': 26397}
        self.testDataPartTwo = {list(self.testDataPartOne.keys())[0]: 288957}

    def ProcessInput(self, data=None):
        """
        
        :param data:
        :returns: processed data for today's challenge
        """
        if not data:
            data = self.rawData

        processed = data.split('\n')

        return processed

    def isLineCorrupted(self, line):
        """
        :param string line: the line to test
        :returns bool, string: if the line is corrupted, and if so which character corrupted the line
        """
        # first collapse the line
        line = self.collapseLine(line)
        for i, char in enumerate(line):
            # don't bother testing if there's nothing left to test at the end of the line
            if i < (len(line) - 2):
                # if the current character is open, and the next character is closed
                # it's a safe bet that the line is corrupted because we should have collapsed
                # the whole line properly by now
                if char in opened and line[i + 1] in closed:
                    return True, line[i+1]

        return False, None

    def collapseLine(self, line):
        """
        Removes interior chunks until the line cannot be collapsed anymore
        :param str line: the line to reduce
        :returns str: the collapsed line
        """
        fully = False
        collapsed = start = line
        while not fully:
            collapsed = start.replace('()', '').replace('{}', '').replace('<>', '').replace('[]', '')
            if collapsed == start:
                fully = True
            start = collapsed

        return collapsed

    def SolvePartOne(self, data=None):
        """
        
        :param data:
        :returns: The solution to today's challenge
        """
        if not data:
            data = self.processed

        corruptionScore = 0
        for line in data:
            corrupted, char = self.isLineCorrupted(line)
            if corrupted:
                corruptionScore += pointTable[char]

        return corruptionScore

    def completeString(self, inString):
        """
        Make the string that would complete the input incomplete string and return it
        """
        # because we have a mapping between the open and closed  characters, just loop through the open characters
        # and replace them with their closed pairings
        for i in opened:
            inString = inString.replace(i, openClose[i])

        # in order to properly close the string, you need to reverse it!
        # but we still want to convert it to a string, we reverse it, convert it to a list
        # then .join it with nothing
        return ''.join(list(reversed(inString)))

    def scoreString(self, inString):
        """
        :param str inString: the completion string
        :return int: the score for the string
        """
        score = 0
        for i in inString:
            score *= 5
            score += pointTablePart2[i]

        return score

    def SolvePartTwo(self, data=None):
        """
        
        :param data:
        :returns: The solution to part two of today's challenge
        """
        if not data:
            data = self.processed

        # just grab all the clea, incomplete lines really quickly
        incompleteLines = [line for line in data if not self.isLineCorrupted(line)[0]]
        # then collapse those lines
        collapsedLines = [self.collapseLine(line) for line in incompleteLines]
        # finally, figure out the string that we'd need to complete the line
        completionStrings = [self.completeString(line) for line in collapsedLines]

        # then score the strings
        scores = [self.scoreString(line) for line in completionStrings]
        scores.sort()

        # we score based of the middle, so half the length round to the nearest integer
        middleScore = scores[int(len(scores) / 2)]

        return middleScore


if __name__ == '__main__':
    day10 = day10Solver()
    day10.Run()
