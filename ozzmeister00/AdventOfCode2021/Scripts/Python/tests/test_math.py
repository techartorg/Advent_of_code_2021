from unittest import TestCase

import utils.math


class Test(TestCase):
    def test_clamp(self):
        testValues = {(2, 3, 4): 3,
                      (3, 2, 4): 3,
                      (4, 2, 3): 3}

        for test, answer in testValues.items():
            self.assertEqual(utils.math.clamp(test[0], test[1], test[2]),
                             answer, msg="Failed to properly clamp {} to {}".format(test, answer))

    def test_saturate(self):
        testValues = {-1.0: 0.0,
                      0.5: 0.5,
                      1.5: 1.0}

        for test, answer in testValues.items():
            self.assertEqual(utils.math.saturate(test), answer,
                             msg="Failed to saturate {} to expected {}".format(test, answer))


class TestTwoD(TestCase):
    def setUp(self):
        self.testValues = 'AB'
        self.otherValues = 'CD'
        self.testObj = utils.math.TwoD(inV=self.testValues, defaultClass=str)
        self.otherObj = utils.math.TwoD(inV=self.otherValues, defaultClass=str)

        self.floatValues = [1.5, 2.5]
        self.otherFloatValues = [.5, 1.5]
        self.testFloatObj = utils.math.Float2(self.floatValues)
        self.otherFloatObj = utils.math.Float2(self.otherFloatValues)

    def test_values(self):
        self.assertEqual(self.testObj.x, self.testValues[0],
                         msg="For some reason {} does not equal A".format(self.testObj.x))
        self.assertEqual(self.testObj.y, self.testValues[1],
                         msg="For some reason {} does not equal B".format(self.testObj.y))

    def test_eq(self):
        self.assertEqual(self.testObj, self.testObj,
                         msg="For some reason {} does not equal itself".format(self.testObj))

        self.assertNotEqual(self.testObj, self.otherObj,
                            msg="For some reason {} equals {}".format(self.testObj, self.otherObj))

    def test_add(self):
        singleAdd = self.testObj + 'A'
        self.assertEqual(singleAdd.x, 'AA',
                         msg="For some reason {} does not equal AA".format(singleAdd.x))
        self.assertEqual(singleAdd.y, 'BA',
                         msg="For some reason {} does not equal BA".format(singleAdd.y))

        sameEquivalent = utils.math.TwoD(['AC', 'BD'], str)
        sameClassAdd = self.testObj + self.otherObj
        self.assertEqual(sameEquivalent, sameClassAdd,
                         msg="For some reason {} does not equal AC,BD".format(sameClassAdd))

        sameClass = self.testFloatObj + self.otherFloatObj
        expected = utils.math.Float2([self.floatValues[0] + self.otherFloatValues[0],
                                      self.floatValues[1] + self.otherFloatValues[1]])
        self.assertEqual(sameClass, expected,
                         msg="For some reason {} does not equal {}".format(sameClass, expected))

        oneD = self.otherFloatObj + .5
        oneDExpected = utils.math.Float2((1.0, 2.0))
        self.assertEqual(oneD, oneDExpected,
                         msg="For some reason {} does not equal {}".format(oneD, oneDExpected))

    def test_mul(self):
        sameClass = self.testFloatObj * self.otherFloatObj
        expected = utils.math.Float2([self.floatValues[0] * self.otherFloatValues[0],
                                      self.floatValues[1] * self.otherFloatValues[1]])
        self.assertEqual(sameClass, expected,
                         msg="For some reason {} does not equal {}".format(sameClass, expected))

        oneD = self.otherFloatObj * 2.0
        oneDExpected = utils.math.Float2((1.0, 3.0))
        self.assertEqual(oneD, oneDExpected,
                         msg="For some reason {} does not equal {}".format(oneD, oneDExpected))

    def test_div(self):
        sameClassDivided = self.testFloatObj / self.otherFloatObj
        expected = utils.math.Float2([self.floatValues[0] / self.otherFloatValues[0],
                                           self.floatValues[1] / self.otherFloatValues[1]])
        self.assertEqual(sameClassDivided, expected,
                         msg="For some reason {} does not equal {}".format(sameClassDivided, expected))

        oneD = self.otherFloatObj / 2.0
        oneDExpected = utils.math.Float2((.25, .75))
        self.assertEqual(oneD, oneDExpected,
                         msg="For some reason {} does not equal {}".format(oneD, oneDExpected))

    def test_sub(self):
        sameClass = self.testFloatObj - self.otherFloatObj
        expected = utils.math.Float2([self.floatValues[0] - self.otherFloatValues[0],
                                           self.floatValues[1] - self.otherFloatValues[1]])
        self.assertEqual(sameClass, expected,
                         msg="For some reason {} does not equal {}".format(sameClass, expected))

        oneD = self.otherFloatObj - .5
        oneDExpected = utils.math.Float2((0.0, 1.0))
        self.assertEqual(oneD, oneDExpected,
                         msg="For some reason {} does not equal {}".format(oneD, oneDExpected))


class TestGrid2D(TestCase):
    def setUp(self):
        self.inGrid = 'ABCD'
        self.testCoords = [(utils.math.Int2((0, 0)), 'A'),
                           (utils.math.Int2((1, 0)), 'B'),
                           (utils.math.Int2((0, 1)), 'C'),
                           (utils.math.Int2((1, 1)), 'D')]

    def test_get(self):
        testObj = utils.math.Grid2D(2, data=self.inGrid)
        for key, value in self.testCoords:
            self.assertEqual(testObj[key], value)

    def test_set(self):
        testObj = utils.math.Grid2D(2, data=self.inGrid)
        target = utils.math.Int2((1, 1))
        testObj[target] = 'E'
        self.assertEqual(testObj[target], 'E')

