class Figure:
    '''Общий класс для фигур'''
    def add_area(self, figure):
        try:
            return self.area + figure.area
        except Exception:
            raise ValueError ('Не передана фигура')
            
            