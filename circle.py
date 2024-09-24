import math

from i_figure import IFigure

class Circle(IFigure):
    def __init__(self, radius):
        assert radius > 0, "Radius must be greater than 0"
        self.radius = radius

    @property
    def square(self):
        return math.pi * self.radius**2