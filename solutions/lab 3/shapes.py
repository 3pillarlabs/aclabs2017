import math
import unittest


class Shape(object):
    def __init__(self, thing):
        self._thing = thing

    def area(self):
        raise NotImplemented()


class Square(Shape):

    @property
    def area(self):
        return self._thing ** 2


class Circle(Shape):
    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter/2)

    @property
    def area(self):
        return self._thing **2  * math.pi


class TestShapes(unittest.TestCase):
    def test_square(self):
        self.assertEqual(Square(10).area, 100)

    def test_circle(self):
        self.assertEqual(Circle(1).area, math.pi)

    def test_circle2(self):
        self.assertEqual(Circle(4).area, 16 * math.pi)

    def test_circle3(self):
        self.assertEqual(Circle.from_diameter(8).area, 16 * math.pi)

