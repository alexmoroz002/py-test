import math

from python_square.i_figure import IFigure

class Triangle(IFigure):
    def __init__(self, a, b, c):
        assert a > 0 and b > 0 and c > 0, "Sides must be greater than 0"

        # Обмен переменных, чтобы в a была наибольшая сторона
        if a < b:
            a,b = b,a
        if a < c:
            a,c = c,a
        assert a < b + c, "Incorrect triangle"

        if math.isclose(b**2 + c**2, a**2):
            self.is_right = True
        else:
            self.is_right = False
        self.a = a
        self.b = b
        self.c = c

    @property
    def square(self):
        if self.is_right:
            return self.b * self.c / 2
        p_half = (self.a + self.b + self.c) / 2
        return math.sqrt(p_half * (p_half - self.a) * (p_half - self.b) * (p_half - self.c))