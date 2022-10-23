from src.figure import Figure


class Square(Figure):
    '''Класс квадрат'''
    def __init__(self, side) -> None:
        NAME = 'square'
        self.name = NAME
        self.side = side
        if not side:
            raise ValueError ('Сторона квадрата не может быть 0')

    @property
    def perimeter(self):
        return self.side * 4

    @property
    def area(self):
        return self.side * self.side

