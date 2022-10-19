from src.circle import Circle


class TestCircle:

    def test_get_area(self):
        circle_1 = Circle(5)
        assert circle_1.area == 19.625, 'Не верно считается площать круга'


    def test_get_perimeter(self):
        circle_1 = Circle(5)
        assert circle_1.perimeter == 15.700000000000001, 'Не верно считается периметр круга'

