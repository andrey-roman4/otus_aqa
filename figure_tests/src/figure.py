class Figure:
    '''Общий класс для фигур'''
    def add_area(self, figure):
        if isinstance(figure, Figure):
            return self.area + figure.area
        else:
            raise ValueError ('Не передана фигура')
            