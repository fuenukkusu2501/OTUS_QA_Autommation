from abc import ABC, abstractmethod


class Figure(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        return (self.side_a + self.side_b) * 2

    def add_area(self, other_figure):
        if not isinstance(other_figure, Figure):
            raise ValueError("Нужен класс Figure")
        return self.get_area() + other_figure.get_area()

