class Figure:
    angles = None
    name = None
    area = None
    perimeter = None

    def __init__(self, name):
        self.name = name

    def setName(self, name):
        self.name = name

    def getAngles(self):
        return self.angles

    def calcArea(self):
        pass

    def calcPerimeter(self):
        pass

    def add_square(self, cl):
        try:
            if isinstance(cl, Figure):
                return self.area + cl.area
        except:
            print('Ошибка')



class Triangle(Figure):
    angles = 3
    side1 = None
    side2 = None
    side3 = None
    height = None

    def setSides(self, side1, side2, side3 ):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def setHeight(self, height):
        self.height = height

    def calcArea(self):
        self.area = 1/2 * self.height * self.side2

    def calcPerimeter(self):
        self.perimeter = self.side1 + self.side2 + self.side3


class Square(Figure):
    angles = 4
    side = None

    def setSideSquare(self, side):
        self.side = side

    def calcArea(self):
        self.area = self.side**2

    def calcPerimeter(self):
        self.perimeter = 4 * self.side



class Rectangle(Figure):
    angles = 4
    side1 = None
    side2 = None

    def setSideRectangle(self, side1, side2):
       self.side1 = side1
       self.side2 = side2

    def calcArea(self):
        self.area = self.side1 * self.side2

    def calcPerimeter(self):
        self.perimeter = 2 * (self.side1 + self.side2)


class Circle(Figure):
    angles = 0
    radius = None

    def radiusCircle(self, radius):
       self.radius = radius

    def calcArea(self):
       self.area = 3.14 * (self.radius ** 2)

    def calcPerimeter(self):
        self.perimeter = 2 * 3.14 * self.radius


