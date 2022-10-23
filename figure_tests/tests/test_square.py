from src.square import Square


class TestSquare:

    def test_get_area(self):
        square_1 = Square(6)
        assert square_1.area == 36, 'Не верно считается площать круга'


    def test_get_perimeter(self):
        square_1 = Square(6)
        assert square_1.perimeter == 24, 'Не верно считается периметр круга'

