from figure import Figure
from rectangle import Rectangle


class Triangle(Figure):

    def __init__(self, side_a, side_b, side_c):
        super().__init__(name="Triangle")
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError("Сторона данной фигуры не должна быть отрицательным или нулевым значением")
        if (side_a + side_b <= side_c) or (side_a + side_c <= side_b) or (side_b + side_c <= side_a):
            raise ValueError("Треугольник не может быть создан с такими параметрами, сумма двух сторон меньше чем третья")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.name = "Triangle"

    def get_area(self):
        p = (self.side_a + self.side_b + self.side_c) / 2
        return (p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c)) ** 0.5

    def get_perimeter(self):
        return self.side_a + self.side_b + self.side_c
