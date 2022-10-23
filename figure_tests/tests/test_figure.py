from src.rectangle import Rectangle
from src.circle import Circle


class TestRectangle:

    def test_get_area(self):
        circle_1 = Circle(5)
        rectangle_1 = Rectangle(5, 7)
        assert rectangle_1.add_area(circle_1) == 54.625, 'Не верно считается сумма площадей'

