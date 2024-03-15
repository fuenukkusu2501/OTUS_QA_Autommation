from rectangle import Rectangle


class Square(Rectangle):

    def __init__(self, side_a):
        if side_a <= 0:
            raise ValueError("Сторона данной фигуры не должна быть отрицательным или нулевым значением")
        super().__init__(side_a)
        self.side_a = side_a
        self.name = "Square"

    def get_area(self):
        return self.side_a * self.side_a

    def get_perimeter(self):
        return self.side_a * 4


s = Square(5)
r = Rectangle(3, 5)
# print(s.add_area(other_figure=r))
# print(s.name)
# print(s.get_area())
# print(r.get_area())
# print(s.get_perimeter())
# print(s)

