from src.rectangle import Rectangle


class TestRectangle:

    def test_get_area(self):
        rectangle_1 = Rectangle(5, 7)
        assert rectangle_1.area == 35, 'Не верно считается площать прямоугольника'


    def test_get_perimeter(self):
        rectangle_1 = Rectangle(5, 7)
        assert rectangle_1.perimeter == 24, 'Не верно считается периметр прямоугольника'

