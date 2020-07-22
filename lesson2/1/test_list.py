import pytest

animals = ['cat',2,3, 'dog','cow']


#1
@pytest.fixture()
def animal_add():
    animals.append('crow')

def test_1(animal_add):

    assert animals==['cat',2,3, 'dog','cow','crow']

#2
@pytest.fixture()
def animal_rev():
    animals.reverse()

def test_2(animal_rev):
    assert animals[2]=='dog'

#3
@pytest.fixture()
def animal_str():
    for i in range(0,len(animals)):
        animals[i]=str(animals[i])

@pytest.fixture()
def animal_sort():
    animals.sort()


def test_3(animal_str,animal_sort):
    print(animals)

#4
@pytest.mark.parametrize('add_list',[1])
def test_4(add_list):
    assert add_list==animals.count('cat')


#5
def test_5():
  assert len(animals)==6