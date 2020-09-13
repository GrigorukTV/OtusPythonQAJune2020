import pytest

from .classes import Triangle, Square, Rectangle, Circle

test_data = [(Square,'Square'),
             (Triangle, 'Triangle'),
             (Rectangle, 'Rectangle'),
             (Circle, 'Circle')]

# создание объекта класса с параметрами и проверка, что свойства устанавливаются корректно
@pytest.mark.parametrize("param_figure", test_data)
def test_param_figure(param_figure):
    cl = param_figure[0]
    n = param_figure[1]
    figure_test = cl(n)
    assert figure_test.name == n

# проверка: тип параметра 'name' = str
@pytest.mark.parametrize("param_figure", test_data)
def test_name (param_figure):
    cl = param_figure[0]
    n = param_figure[1]
    figure_test = cl(n)
    assert (type(figure_test.name) is str) == True

# проверка количетсва углов в фигуре
@pytest.mark.parametrize("angles_figure", [(Square,4),
                                           (Triangle, 3),
                                           (Rectangle, 4),
                                           (Circle, 0)])
def test_angles(angles_figure):
    cl = angles_figure [0]
    sum_angles = angles_figure [1]
    figure_test = cl('')
    assert figure_test.angles == sum_angles


# проверка: площадь фигур
# площадь треугольника > суммы сторон треугольника
test_data_Triangle = [('Triangle1',3,1,1,11),
             ('Triangle2',23,33,44,55),
             ('Triangle3',5,6,3,8),
             ('Triangle4',9,4,4,20)]


@pytest.mark.parametrize("param_figure", test_data_Triangle)
def test_area_t (param_figure):
    n = param_figure[0]
    s1 = param_figure[1]
    s2 = param_figure[2]
    s3 = param_figure[3]
    h = param_figure[4]

    tri = Triangle(n)
    tri.setSides(s1, s2, s3)
    tri.setHeight(h)

    tri.calcArea()
    assert tri.area > s1 + s2 + s3


# площадь квадрата > стороны квадрата
test_data_Square = [('Square3',5),
                    ('Square4',9)]

@pytest.mark.parametrize("param_figure", test_data_Square)
def test_area_s (param_figure):
    n = param_figure[0]
    s1 = param_figure[1]

    squ = Square(n)
    squ.setSideSquare(s1)

    squ.calcArea()
    assert squ.area > s1

# площадь прямоугольника > суммы сторон прямоугольника
test_data_Rectangle= [('Rectangle1',11,12),
             ('Rectangle2',23,33),
             ('Rectangle3',5,6),
             ('Rectangle4',9,8)]

@pytest.mark.parametrize("param_figure", test_data_Rectangle)
def test_area_r (param_figure):
    n = param_figure[0]
    s1 = param_figure[1]
    s2 = param_figure [2]

    rec = Rectangle(n)
    rec.setSideRectangle(s1, s2)

    rec.calcArea()
    assert rec.area > s1 + s2

# площадь круга > радиуса круга
test_data_Circle = [('Circle1',11),
             ('Circle2',23),
             ('Circle3',5),
             ('Circle4',9)]

@pytest.mark.parametrize("param_figure", test_data_Circle)
def test_area_c (param_figure):
    n = param_figure[0]
    r = param_figure[1]

    circ = Circle(n)
    circ.radiusCircle(r)

    circ.calcArea()
    assert circ.area > r
# проверка: периметр фигур
# периметр треугольника > одной стороны треугольника
test_data_Triangle = [('Triangle1',3,1,1),
             ('Triangle2',23,33,44),
             ('Triangle3',5,6,3),
             ('Triangle4',9,4,4)]


@pytest.mark.parametrize("param_figure", test_data_Triangle)
def test_perimeter_t (param_figure):
    n = param_figure[0]
    s1 = param_figure[1]
    s2 = param_figure[2]
    s3 = param_figure[3]

    tri = Triangle(n)
    tri.setSides(s1, s2, s3)

    tri.calcPerimeter()
    assert tri.perimeter > s1


# периметр квадрата > стороны квадрата
test_data_Square = [('Square1',11),
             ('Square2',23),
             ('Square3',5),
             ('Square4',9)]

@pytest.mark.parametrize("param_figure", test_data_Square)
def test_perimeter_s (param_figure):
    n = param_figure[0]
    s1 = param_figure[1]

    squ = Square(n)
    squ.setSideSquare(s1)

    squ.calcPerimeter()
    assert squ.perimeter > s1

# периметр прямоугольника > стороны прямоугольника
@pytest.mark.parametrize("param_figure", test_data_Rectangle)
def test_perimeter_r (param_figure):
    n = param_figure[0]
    s1 = param_figure[1]
    s2 = param_figure [2]

    rec = Rectangle(n)
    rec.setSideRectangle(s1, s2)

    rec.calcPerimeter()
    assert rec.perimeter > s1

# периметр круга > радиуса круга
@pytest.mark.parametrize("param_figure", test_data_Circle)
def test_perimeter_c (param_figure):
    n = param_figure[0]
    r = param_figure[1]

    circ = Circle(n)
    circ.radiusCircle(r)

    circ.calcPerimeter()
    assert circ.perimeter > r


# проверка: сумма площадей фигур > площади фигуры

test_data_compare_areas = [({'side1': 2, 'side2': 3, 'side3': 4, 'height': 5}, {"side": 6}, {"radius": 7})]
@pytest.mark.parametrize("param_figure", test_data_compare_areas)
def test_add_square_area(param_figure):
    firstClassParams = param_figure[0]
    secondClassParams = param_figure[1]
    thirdClassParams = param_figure[2]


    tri = Triangle('Треугольник')
    tri.setSides(firstClassParams['side1'], firstClassParams['side2'], firstClassParams['side3'])
    tri.setHeight(firstClassParams['height'])
    tri.calcArea()

    squ = Square('Квадрат')
    squ.setSideSquare(secondClassParams['side'])
    squ.calcArea()

    cir = Circle('Круг')
    cir.radiusCircle(thirdClassParams['radius'])
    cir.calcArea()

    assert tri.add_square(squ) == tri.area + squ.area
    assert cir.add_square(tri) == tri.area + cir.area