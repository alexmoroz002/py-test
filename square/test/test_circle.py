import math
from unittest import TestCase

from square.circle import Circle


class TestCircle(TestCase):
    def test_square_ok(self):
        params = [0.1, 5, 10000.003]
        res = [0.0314, 78.5398, 314159453.8546]
        for radius, real_square in zip(params, res):
            with self.subTest(radius, real_square=real_square):
                circle = Circle(radius)
                self.assertAlmostEqual(circle.square, real_square, delta=0.0001)

    def test_radius_zero(self):
        self.assertRaises(AssertionError, Circle, 0)

    def test_radius_negative(self):
        self.assertRaises(AssertionError, Circle, -5)