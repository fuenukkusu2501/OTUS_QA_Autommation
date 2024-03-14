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









# s = Square(5)
# r = Rectangle(3, 5)
# print(r.add_area(other_figure=s))

# print(s.get_area())
# print(s.get_perimeter())

#     def get_area(s1, s2, sep)
#     def get_perimeter()
#
#     def add_area(figure)
#
# def get_area(s1, s2, sep):
#     print(s1 * sep * s2)

# if not isinstance(other_figure, Rectangle) - написать ошибку для треугольника, что там должно быть только 3 стороны
# + загуглять, что делает треугольник треугольником какие-то правила, по размерам тех ли других сторон, вобщем,
# что делает треугольник треугольником.