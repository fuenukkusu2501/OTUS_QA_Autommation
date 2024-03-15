from figure import Figure
import math


class Circle(Figure):

    def __init__(self, radius):
        super().__init__(name="Circle")
        if radius <= 0:
            raise ValueError("Сторона данной фигуры не должна быть отрицательным или нулевым значением")
        self.radius = radius
        self.name = "Circle"

    def get_area(self):
        return math.pi * self.radius ** 2

    def get_perimeter(self):
        return 2 * (math.pi * self.radius)
    