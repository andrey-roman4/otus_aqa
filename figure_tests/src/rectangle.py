from src.figure import Figure


class Rectangle(Figure):
    '''Класс прямоугольник'''
    def __init__(self, s_1, s_2) -> None:
        NAME = 'rectangle'
        self.s_1 = s_1
        self.s_2 = s_2
        self.name = NAME
        if not s_1 or not s_2:
            raise ValueError ('Сторона прямоугольника не может быть 0') 

    @property
    def perimeter(self):
        return (self.s_1 + self.s_2) * 2

    @property
    def area(self):        
        return self.s_1 * self.s_2

