from figure import Figure


class Rectangle(Figure):

    def __init__(self, side_a, side_b):
        super().__init__(name="Rectangle")
        if side_a <= 0 or side_b <= 0:
            raise ValueError("Сторона прямоугольника не должна быть отрицательным или нулевым значением")
        self.side_a = side_a
        self.side_b = side_b

    def get_area(self):
        return self.side_a * self.side_b

    def get_perimeter(self):
        return (self.side_a + self.side_b) * 2

# a = Rectangle(3,5)
# print(a.side_a)
# print(a.side_b)
# print(a.get_area())
# print(a.get_perimeter())









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