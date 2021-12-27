"""
Common maths functions and datatypes for solving Advent of Code problems
"""

import functools
import operator


def saturate(value):
    """
    Saturates a value, so it is only ever between 0 and 1

    :param float value: the value to saturate

    :return float: the value, but clamped between 0 and 1
    """
    return clamp(value, 0.0, 1.0)


def clamp(value, minValue, maxValue):
    """
    Returns a value that is no less than the min value, and no more than the max value

    :param float value: the value to clamp
    :param float minValue: the minimum value to return
    :param float maxValue: the maximum value to return

    :return float: the clamped value
    """
    return max(minValue, min(value, maxValue))


def product(iterable):
    """
    Returns the product of an iterable of numbers
    :param list iterable: eg [1, 2, 3, 4, 5]
    :return float: the product of all items in the iterable multiplied together
    """
    return functools.reduce(operator.mul, iterable, 1)


class TwoD(list):
    """
    A TwoD object to make it easier to access and multiply 2-length lists of numbers
    """
    def __init__(self, inV=None, defaultClass=None):
        """
        :param class baseClass: which datatype class to use to instantiate the array
        :param iterable inV: two-length iterable of class defaultClass
        """
        # set up a default input value to instatiate a float 2 to 0,0 automatically
        # because we can't put a [0,0] in the kwargs otherwise it'll be the same
        # for every instance and that's no bueno
        if not inV:
            inV = [defaultClass(), defaultClass()]
        else:
            inV = [defaultClass(v) for v in inV]  # convert our inputData to a list

        self.defaultClass = defaultClass

        super(TwoD, self).__init__(inV)

    def __add__(self, other):
        if isinstance(other, TwoD):
            return self.__class__([self.x + other.x, self.y + other.y], defaultClass=self.defaultClass)
        else:
            return self.__class__([self.x + other, self.y + other], defaultClass=self.defaultClass)

    def __sub__(self, other):
        if isinstance(other, TwoD):
            return self.__class__([self.x - other.x, self.y - other.y], defaultClass=self.defaultClass)
        else:
            return self.__class__([self.x - other, self.y - other], defaultClass=self.defaultClass)

    def __mul__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__([self.x * other.x, self.y * other.y], defaultClass=self.defaultClass)
        if isinstance(other, int) or isinstance(other, float):
            return self.__class__([self.x * other, self.y * other], defaultClass=self.defaultClass)

    def _div(self, other):
        if isinstance(other, self.__class__):
            return self.__class__([self.x / other.x, self.y / other.y], defaultClass=self.defaultClass)
        if isinstance(other, int) or isinstance(other, float):
            return self.__class__([self.x / other, self.y / other], defaultClass=self.defaultClass)

    def __truediv__(self, other):
        return self._div(other)

    def __divmod__(self, other):
        return self._div(other)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            if self.x == other.x and self.y == other.y:
                return True

        return False

    @property
    def x(self):
        """
        Access the first, X value of the list
        :return float:
        """
        return self[0]

    @x.setter
    def x(self, v):
        self[0] = v

    @property
    def y(self):
        """
        The second, Y value of the list
        :return float:
        """
        return self[1]

    @y.setter
    def y(self, v):
        self[1] = v


class Float2(TwoD):
    """
    Float-specific alias for TwoD
    """
    def __init__(self, inV=None, defaultClass=float):
        super(Float2, self).__init__(inV, defaultClass=float)


class Int2(TwoD):
    """
    Alias for TwoD
    """
    def __init__(self, inV=None, defaultClass=int):
        super(Int2, self).__init__(inV, defaultClass=int)


def dot(a, b):
    """
    :param list a: list of numbers
    :param list b: list of numbers equal in length to the first list
    :return float: dot product of n-length lists of numbers
    """
    if len(a) != len(b):
        raise ValueError("Input lists must be of equal length (got {} and {})".format(len(a), len(b)))

    return sum([x * y for x, y in zip(a, b)])


def getBarycentric(p, a, b, c):
    """
    Get the barycentric coordinates of cartesin point a in
    reference frame abc

    :param Float2 p: test point
    :param Float2 a: point A
    :param Float2 b: point B
    :param Float2 c: point C

    :return list: the UVW coordinate of cartesian point P in reference frame created by points ABC
    """
    v0 = b - a  # Vector BA
    v1 = c - a  # Vector CA
    v2 = p - a  # Vector PA
    d00 = dot(v0, v0)  # dot BA . BA
    d01 = dot(v0, v1)  # dot BA . CA
    d11 = dot(v1, v1)  # dot CA . CA
    d20 = dot(v2, v0)  # dot PA . BA
    d21 = dot(v2, v1)  # dot PA . CA

    denom = (d00 * d11) - (d01 * d01)

    v = (d11 * d20 - d01 * d21) / denom
    w = (d00 * d21 - d01 * d20) / denom
    u = 1.0 - v - w

    return u, v, w


class Grid2D(list):
    def __init__(self, width, data=None):
        """
        :param int width: how wide is the 2D Grid
        :param iterable data: a 1d iterable with which to instantiate the grid
        """
        super(Grid2D, self).__init__(data)
        self.width = width

    @property
    def height(self):
        """
        Get the height of the Grid2D
        :return int:
        """
        return int(len(self) / self.width)

    @height.setter
    def height(self, value):
        """
        Grid2D doesn't support resizing yet
        """
        pass

    def _coordsToIndex(self, coords):
        """
        :param Int2 coords: the 2d coordinates to translate to 1d

        :return int: 1d index
        """
        return coords.y * self.width + coords.x

    def __getitem__(self, coords):
        """
        :param Int2 coords: the coordinates of the item to retrieve

        :returns: the item at the input coordinates
        """
        return super(Grid2D, self).__getitem__(self._coordsToIndex(coords))

    def __setitem__(self, coords, value):
        """
        :param Int2 coords: the coordinates of the item to set
        :param value: the value to which to set the coordinates
        """
        super(Grid2D, self).__setitem__(self._coordsToIndex(coords), value)

    def __delitem__(self, coords):
        """
        :param Int2 coords: the coordinates of the item to delete
        """
        super(Grid2D, self).__delitem__(self._coordsToIndex(coords))

    def __str__(self):
        outString = ''
        for y in range(self.height):
            for x in range(self.width):
                outString += str(self[Int2((x, y))]) + " "
            outString += '\n'

        return outString







