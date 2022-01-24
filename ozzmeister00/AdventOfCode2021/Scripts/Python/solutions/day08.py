"""
--- Day 8: Seven Segment Search ---
You barely reach the safety of the cave when the
whale smashes into the cave mouth, collapsing it.
Sensors indicate another exit to this cave at a much
greater depth, so you have no choice but to press on.

As your submarine slowly makes its way through the
cave system, you notice that the four-digit seven-segment
displays in your submarine are malfunctioning;
they must have been damaged during the escape.
You'll be in a lot of trouble without them,
so you'd better figure out what's wrong.

Each digit of a seven-segment display is rendered by
 turning on or off any of seven segments named a through g:

  0:      1:      2:      3:      4:
 aaaa    ....    aaaa    aaaa    ....
b    c  .    c  .    c  .    c  b    c
b    c  .    c  .    c  .    c  b    c
 ....    ....    dddd    dddd    dddd
e    f  .    f  e    .  .    f  .    f
e    f  .    f  e    .  .    f  .    f
 gggg    ....    gggg    gggg    ....

  5:      6:      7:      8:      9:
 aaaa    aaaa    aaaa    aaaa    aaaa
b    .  b    .  .    c  b    c  b    c
b    .  b    .  .    c  b    c  b    c
 dddd    dddd    ....    dddd    dddd
.    f  e    f  .    f  e    f  .    f
.    f  e    f  .    f  e    f  .    f
 gggg    gggg    ....    gggg    gggg
So, to render a 1, only segments c and f would be turned on;
 the rest would be off. To render a 7, only segments a, c,
  and f would be turned on.

The problem is that the signals which control the
segments have been mixed up on each display.
The submarine is still trying to display numbers
by producing output on signal wires a through g,
but those wires are connected to segments randomly.
Worse, the wire/segment connections are mixed up separately
 for each four-digit display! (All of the digits
 within a display use the same connections, though.)

So, you might know that only signal wires b and g are turned
on, but that doesn't mean segments b and g are turned on:
 the only digit that uses two segments is 1, so it must mean
  segments c and f are meant to be on. With just that
  information, you still can't tell which wire (b/g)
  goes to which segment (c/f). For that, you'll need
  to collect more information.

For each display, you watch the changing signals for a while,
 make a note of all ten unique signal patterns you see,
 and then write down a single four digit output value (your puzzle input).
  Using the signal patterns, you should be able to work out which pattern corresponds to which digit.

For example, here is what you might see in a single entry in your notes:

acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf
(The entry is wrapped here to two lines so it fits; in your notes, it will all be on a single line.)

Each entry consists of ten unique signal patterns, a | delimiter,
and finally the four digit output value. Within an entry,
the same wire/segment connections are used (but you don't know
what the connections actually are). The unique signal patterns
correspond to the ten different ways the submarine tries to
render a digit using the current wire/segment connections.
Because 7 is the only digit that uses three segments,
dab in the above example means that to render a 7, signal lines
 d, a, and b are on. Because 4 is the only digit that uses
  four segments, eafb means that to render a 4, signal lines e, a, f, and b are on.

Using this information, you should be able to work out which
 combination of signal wires corresponds to each of the ten digits.
 Then, you can decode the four digit output value. Unfortunately,
 in the above example, all of the digits in the output value
 (cdfeb fcadb cdfeb cdbaf) use five segments and are more difficult to deduce.

For now, focus on the easy digits. Consider this larger example:

be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
Because the digits 1, 4, 7, and 8 each use a unique number of segments,
you should be able to tell which combinations of signals correspond to those digits.
 Counting only digits in the output values (the part after | on each line),
 in the above example, there are 26 instances of digits that use a
  unique number of segments (highlighted above).

In the output values, how many times do digits 1, 4, 7, or 8 appear?

To begin, get your puzzle input.
"""
import string

from utils.solver import ProblemSolver

# we know that these four unique lengths of segments
# correspond to these specific digits
KnownDigitLengths = {2: 1,
               4: 4,
               3: 7,
               7: 8}


class DisplayDigit(object):
    def __init__(self, segments):
        # initialize each of the segments to False
        self.segments = [False] * 7

        # loop over the active segments for this digit and set those to True
        for i in segments:
            self.segments[string.ascii_lowercase.find(i)] = True

        # stash off the raw segments in case we need them later
        self.rawSegments = segments

        # god willing, we know what integer this corresponds to
        self.digit = -1
        self.determineInteger()

        self.displayOrder = [0, 1, 2, 3, 4, 5, 6]

    def determineInteger(self):
        """
        Use the input raw segments to see if we can figure out which digit this corresponds to
        """
        if len(self.rawSegments) in KnownDigitLengths:
            self.digit = KnownDigitLengths[len(self.rawSegments)]

    def getSegmentString(self, i):
        return '#' if self.segments[self.displayOrder[i]] else ' '

    def __str__(self):
        outStr = ' {0}{0}{0}{0} \n'.format(self.getSegmentString(0))
        for i in range(2):
            outStr += '{0}    {1}\n'.format(self.getSegmentString(1), self.getSegmentString(2))
        outStr += ' {0}{0}{0}{0} \n'.format(self.getSegmentString(3))
        for i in range(2):
            outStr += '{0}    {1}\n'.format(self.getSegmentString(4), self.getSegmentString(5))
        outStr += ' {0}{0}{0}{0} \n'.format(self.getSegmentString(6))
        return outStr

    def __eq__(self, other):
        if isinstance(other, str):
            return self.rawSegments == other
        elif isinstance(other, int):
            return self.digit == other
        elif isinstance(other, list):
            return self.segments == other

        return False

    def __repr__(self):
        return 'DisplayDigit("{}")'.format(self.rawSegments)


class LogEntry(object):
    def __init__(self, inString):
        uniqueEntries, displayed = inString.split(' | ')
        # store off all the unique configurations
        self.uniqueEntries = [DisplayDigit(i) for i in uniqueEntries.split(' ')]
        self.displayed = [DisplayDigit(i) for i in displayed.split(' ')]

    def __repr__(self):
        entries = ' '.join([repr(i) for i in self.uniqueEntries])
        displayed = ' '.join([repr(i) for i in self.displayed])
        return 'LogEntry("{} | {}")'.format(entries, displayed)


class day08Solver(ProblemSolver):
    def __init__(self):
        super(day08Solver, self).__init__(8)

        self.testDataPartOne = {'acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf': 0,
                                '''be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce''': 26
                                }
        self.testDataPartTwo = {'''acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf''': 5353,
                                list(self.testDataPartOne.keys())[1]: 61229}

    def ProcessInput(self, data=None):
        """
        
        :param data:
        :returns: processed data for today's challenge
        """
        if not data:
            data = self.rawData

        processed = [LogEntry(i) for i in data.split('\n')]

        return processed

    def SolvePartOne(self, data=None):
        """
        In the output values, how many times do digits 1, 4, 7, or 8 appear?

        :param list[LogEntry] data:
        :returns: The solution to today's challenge
        """
        if not data:
            data = self.processed

        count = 0
        for i in data:
            count += i.displayed.count(1)
            count += i.displayed.count(4)
            count += i.displayed.count(7)
            count += i.displayed.count(8)

        return count

    def determineDisplayOrder(self, entry):
        """
        :param LogEntry entry: the entry to try and suss out
        :return list: the segment display order
        """
        def setIncludesSet(a, b):
            return all([True if i in b else False for i in a])

        one = set(entry.uniqueEntries[entry.uniqueEntries.index(1)].rawSegments)
        four = set(entry.uniqueEntries[entry.uniqueEntries.index(4)].rawSegments)
        seven = set(entry.uniqueEntries[entry.uniqueEntries.index(7)].rawSegments)
        eight = set(entry.uniqueEntries[entry.uniqueEntries.index(8)].rawSegments)

        # we know that the topmost segment is the seven segments without the one segment
        a = seven.difference(one)
        # and the middle+topleft segments are four without the one segments
        bd = four.difference(one)

        # stash off all the six-length segments to make it easier on ourselves
        sixLong = [set(i.rawSegments) for i in entry.uniqueEntries if len(i.rawSegments) == 6]

        six = a.union(bd)
        for i in sixLong:
            # of the three sets that are 6-long, the one that doesn't fully contain one is six
            if not setIncludesSet(one, i):
                six = i

        assert len(six) == 6, "Six is not of length six"

        c = one.difference(six)
        f = one.difference(c)
        eg = six.difference(four).difference(a)

        # now that we know which one is six, we can pop it out of the sixlongs
        sixLong.pop(sixLong.index(six))

        # then we can figure out which one is nine, because it's the only remaining set
        # of six-length combinations that includes D
        nine = a.union(bd).union(one)
        for i in sixLong:
            if setIncludesSet(nine, i):
                nine = i

        assert len(nine) == 6, "Nine is not of length six"
        sixLong.pop(sixLong.index(nine))
        # which means that the remaining six-length combination must be zero
        zero = sixLong[0]

        # and we know that D is eight minus zero
        d = eight.difference(zero)

        # and we know that eight minus nine is e
        e = eight.difference(nine)

        # so we can cull d from bd to get b
        b = bd.difference(d)

        # and finally we have g from eg
        g = eg.difference(e)

        # now we can construct two, three, and five since we know all the individual characters
        five = a.union(bd).union(f).union(g)
        two = a.union(c).union(d).union(eg)
        three = seven.union(d).union(g)
        return [zero, one, two, three, four, five, six, seven, eight, nine]

    def SolvePartTwo(self, data=None):
        """
        
        :param data:
        :returns: The solution to part two of today's challenge
        """
        if not data:
            data = self.processed

        sumValues = 0
        for entry in data:
            numbers = self.determineDisplayOrder(entry)
            values = []
            for i in entry.displayed:
                values.append(numbers.index(set(i.rawSegments)))

            values = int(''.join([str(i) for i in values]))
            sumValues += values

        print(type(sumValues))

        return sumValues


if __name__ == '__main__':
    day08 = day08Solver()
    day08.Run()
