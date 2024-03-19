import pytest

from src.rectangle import Rectangle
from src.triangle import Triangle
from src.circle import Circle
from src.square import Square


"""Позитивные тесты на площадь"""


@pytest.mark.parametrize("rectangle_data_1", ["integer_area", "float_area"])
def test_area_rectangle_positiv(rectangle_data, rectangle_data_1):
    side_a, side_b, area = rectangle_data(data=rectangle_data_1)
    r = Rectangle(side_a, side_b)
    assert r.get_area() == area, f"Area shold be {area}"


@pytest.mark.parametrize("square_data_1", ["integer_area", "float_area"])
def test_area_square_positiv(square_data, square_data_1):
    side_a, area = square_data(data=square_data_1)
    s = Square(side_a)
    assert s.get_area() == area, f"Area shold be {area}"


@pytest.mark.parametrize("triangle_data_1", ["integer_area", "float_area"])
def test_area_triangle_positiv(triangle_data, triangle_data_1):
    side_a, side_b, side_c, area = triangle_data(data=triangle_data_1)
    t = Triangle(side_a, side_b, side_c)
    assert t.get_area() == area, f"Area shold be {area}"


@pytest.mark.parametrize("circle_data_1", ["integer_area", "float_area"])
def test_area_circle_positiv(circle_data, circle_data_1):
    radius, area = circle_data(data=circle_data_1)
    c = Circle(radius)
    assert c.get_area() == area, f"Area shold be {area}"


"""Позитивные тесты на периметр"""


@pytest.mark.parametrize("rectangle_data_1", ["integer_perimeter", "float_perimeter"])
def test_area_rectangle_positiv(rectangle_data, rectangle_data_1):
    side_a, side_b, perimeter = rectangle_data(data=rectangle_data_1)
    r = Rectangle(side_a, side_b)
    assert r.get_perimeter() == perimeter, f"Area shold be {perimeter}"


@pytest.mark.parametrize("square_data_1", ["integer_perimeter", "float_perimeter"])
def test_area_square_positiv(square_data, square_data_1):
    side_a, perimeter = square_data(data=square_data_1)
    s = Square(side_a)
    assert s.get_perimeter() == perimeter, f"Area shold be {perimeter}"


@pytest.mark.parametrize("triangle_data_1", ["integer_perimeter", "float_perimeter"])
def test_area_triangle_positiv(triangle_data, triangle_data_1):
    side_a, side_b, side_c, perimeter = triangle_data(data=triangle_data_1)
    t = Triangle(side_a, side_b, side_c)
    assert t.get_perimeter() == perimeter, f"Area shold be {perimeter}"


@pytest.mark.parametrize("circle_data_1", ["integer_perimeter", "float_perimeter"])
def test_area_circle_positiv(circle_data, circle_data_1):
    radius, perimeter = circle_data(data=circle_data_1)
    c = Circle(radius)
    assert c.get_perimeter() == perimeter, f"Area shold be {perimeter}"


"""Негативные тесты"""


@pytest.mark.parametrize("rectangle_data_1", ["minus", "zero"])
def test_rectangle_negative(rectangle_data, rectangle_data_1):
    side_a, side_b = rectangle_data(data=rectangle_data_1)
    with pytest.raises((ValueError)):
        Rectangle(side_a, side_b)


@pytest.mark.parametrize("square_data_1", ["minus", "zero"])
def test_square_negative(square_data, square_data_1):
    side_a = square_data(data=square_data_1)
    with pytest.raises((ValueError)):
        Square(side_a)


@pytest.mark.parametrize("triangle_data_1", ["minus", "zero"])
def test_triangle_negative(triangle_data, triangle_data_1):
    side_a, side_b, side_c = triangle_data(data=triangle_data_1)
    with pytest.raises((ValueError)):
        Triangle(side_a, side_b, side_c)


@pytest.mark.parametrize("circle_data_1", ["minus", "zero"])
def test_circle_negative(circle_data, circle_data_1):
    radius = circle_data(data=circle_data_1)
    with pytest.raises((ValueError)):
        Circle(radius)


@pytest.mark.parametrize("triangle_data_1", ["a + b < c", "a + b = c"])
def test_triangle_negative_is_valid(triangle_data, triangle_data_1):
    side_a, side_b, side_c = triangle_data(data=triangle_data_1)
    with pytest.raises((ValueError)):
        Triangle(side_a, side_b, side_c)


#pytest --setup-plan