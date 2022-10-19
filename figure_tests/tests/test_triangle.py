from src.triangle import Triangle


class TestTriangle:

    def test_get_area(self):
        triangle_1 = Triangle(4, 2, 4)
        assert triangle_1.area == 3.872983346207417, 'Не верно считается площать треугольника'


    def test_get_perimeter(self):
        triangle_1 = Triangle(4, 2, 4)
        assert triangle_1.perimeter == 10, 'Не верно считается периметр треугольника'

