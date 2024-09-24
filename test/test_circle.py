import math
from unittest import TestCase

from circle import Circle


class TestCircle(TestCase):
    def test_square_ok(self):
        params = [0.1, 5, 10000.003]
        for radius in params:
            with self.subTest(radius):
                circle = Circle(radius)
                self.assertAlmostEqual(circle.square, radius**2 * math.pi, delta=0.0001)

    def test_radius_zero(self):
        self.assertRaises(AssertionError, Circle, 0)

    def test_radius_negative(self):
        self.assertRaises(AssertionError, Circle, -5)