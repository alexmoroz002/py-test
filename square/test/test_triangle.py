from unittest import TestCase

from square.triangle import Triangle


class TestTriangle(TestCase):
    def test_square_ok(self):
        sides_list = [(3, 4, 5), (0.5, 8, 8.49), (4, 4, 4)]
        real_squares = [6, 0.41, 6.9282]
        for sides, real_square in zip(sides_list, real_squares):
            with self.subTest(sides=sides, real_square=real_square):
                triangle = Triangle(*sides)
                self.assertAlmostEqual(triangle.square, real_square, delta=0.0001)

    def test_triangle_right(self):
        a, b, c = 3, 4, 5
        self.assertTrue(Triangle(a, b, c).is_right)

    def test_sides_incorrect(self):
        a, b, c = 1, 2, 3
        self.assertRaises(AssertionError, Triangle, a, b, c)

    def test_sides_negative(self):
        a, b, c = -1, 2, 3
        self.assertRaises(AssertionError, Triangle, a, b, c)