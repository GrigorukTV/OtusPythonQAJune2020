class Figure:
    angles = None

    def __init__(self, name, area, perimeter):
        self.name = name
        self.area = area
        self.perimeter = perimeter

    def setName(self, name):
        self.name = name

    def setArea(self, area):
        self.area = area

    def setPerimeter(self, perimeter):
        self.perimeter = perimeter

    def getAngles(self):
        return self.angles

    def add_square(self, cl):
        try:
            if isinstance(cl, Figure):
                return self.area + cl.area
        except:
            print('Ошибка')


class Triangle(Figure):
    angles = 3


class Square(Figure):
   angles = 4


class Rectangle(Figure):
   angles = 4


class Circle(Figure):
   angles = 0
