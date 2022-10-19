from src.figure import Figure


class Triangle(Figure):
    '''Класс треугольник'''
    def __init__(self, s_1, s_2, s_3) -> None:
        NAME = 'triangle'
        self.s_1 = s_1
        self.s_2 = s_2
        self.s_3 = s_3
        self.name = NAME
        if not s_1 or not s_2 or not s_3:
            raise ValueError ('Сторона треугольника не может быть 0')
        if self.s_1 + self.s_2 < self.s_3 or self.s_1 + self.s_3 < self.s_2 or self.s_2 + self.s_3 < self.s_1:
            raise ValueError ('Неверные стороны треугольника')


    @property
    def perimeter(self):
        return self.s_1 + self.s_2 + self.s_3

    @property
    def area(self):
        half_perimetr = self.perimeter / 2
        area = (half_perimetr * (half_perimetr - self.s_1) * (half_perimetr - self.s_2) * (half_perimetr - self.s_3)) ** 0.5
        return area

