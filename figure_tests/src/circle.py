from src.figure import Figure


class Circle(Figure):
    '''Класс круг'''
    def __init__(self, d) -> None:
        NAME = 'circle'
        self.d = d
        self.name = NAME
        if not d:
            raise ValueError ('Диаметр круга не может быть 0') 

    @property
    def perimeter(self):
        return 3.14 * self.d

    @property
    def area(self):
        return ((self.d * self.d) / 4) * 3.14 

