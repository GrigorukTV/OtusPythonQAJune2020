import pytest

from .classes import Triangle, Square, Rectangle, Circle

test_data = [(Square,'Square', 1, 3),
             (Triangle, 'Triangle', 2, 8),
             (Rectangle, 'Rectangle', 3, 8),
             (Circle, 'Circle', 4, 8)]

# создание объекта класса с параметрами и проверка, что свойства устанавливаются корректно
@pytest.mark.parametrize("param_figure", test_data)
def test_param_figure(param_figure):

    cl = param_figure[0]
    n = param_figure[1]
    a = param_figure[2]
    p = param_figure[3]

    figure_test = cl(n, a, p)

    assert figure_test.name == n
    assert figure_test.area == a
    assert figure_test.perimeter == p

# проверка: площадь фигуры > 0
@pytest.mark.parametrize("param_figure", test_data)
def test_area (param_figure):
    cl = param_figure[0]
    n = param_figure[1]
    a = param_figure[2]
    p = param_figure[3]

    figure_test = cl(n, a, p)
    assert figure_test.area > 0

# проверка: периметр фигуры > 0
@pytest.mark.parametrize("param_figure", test_data)
def test_perimeter (param_figure):
    cl = param_figure[0]
    n = param_figure[1]
    a = param_figure[2]
    p = param_figure[3]

    figure_test = cl(n, a, p)
    assert figure_test.perimeter > 0

# проверка: тип параметра 'name' = str
@pytest.mark.parametrize("param_figure", test_data)
def test_name (param_figure):
    cl = param_figure[0]
    n = param_figure[1]
    a = param_figure[2]
    p = param_figure[3]

    figure_test = cl(n, a, p)
    assert (type(figure_test.name) is str) == True

# проверка количетсва углов в фигуре
@pytest.mark.parametrize("angles_figure", [(Square,4),
                                           (Triangle, 3),
                                           (Rectangle, 4),
                                           (Circle, 0)])
def test_angles(angles_figure):
    cl = angles_figure [0]
    sum_angles = angles_figure [1]
    figure_test = cl('', 0, 0)
    assert figure_test.angles == sum_angles


# проверка: сумма площадей фигур > 0
@pytest.mark.parametrize("param_figure", test_data)
def test_add_square(param_figure):
    cl = param_figure[0]
    n = param_figure[1]
    a = param_figure[2]
    p = param_figure[3]

    figure_test = cl(n, a, p)
    figure_test_add = Triangle('Triangle', 2, 8)
    s = figure_test.add_square(figure_test_add)
    assert s > 0

# проверка: тип сумма площадей фигур = int
@pytest.mark.parametrize("param_figure", test_data)
def test_add_square_type (param_figure):
    cl = param_figure[0]
    n = param_figure[1]
    a = param_figure[2]
    p = param_figure[3]

    figure_test = cl(n, a, p)
    figure_test_add = Triangle('Triangle', 2, 8)
    s = figure_test.add_square(figure_test_add)
    assert (type(s) is int) == True

# проверка: сумма площадей фигур > площади фигуры
@pytest.mark.parametrize("param_figure", test_data)
def test_add_square_area(param_figure):
    cl = param_figure[0]
    n = param_figure[1]
    a = param_figure[2]
    p = param_figure[3]

    figure_test = cl(n, a, p)
    figure_test_add = Triangle('Triangle', 2, 8)
    s = figure_test.add_square(figure_test_add)
    assert s > a

# проверка сеттера
@pytest.mark.parametrize("param_figure", test_data)
def test_name (param_figure):
    cl = param_figure[0]
    n = param_figure[1]
    a = param_figure[2]
    p = param_figure[3]

    figure_test = cl(n, a, p)
    figure_test.setName('Test')
    assert figure_test.name == 'Test'




