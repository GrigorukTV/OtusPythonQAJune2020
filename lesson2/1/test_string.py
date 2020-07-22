import pytest


test="Good afternoon"


#1
def test_1():
    assert test.find("f")

#2
@pytest.fixture()
def test_len():
    return len(test)

def test_2(test_len):
    assert test_len==14

#3
def test_3():
    assert test[1:3]=="oo"
#4
@pytest.fixture()
def test_upper():
    return test.upper()

def test_4(test_upper):
    assert test_upper=="GOOD AFTERNOON"

#5
@pytest.mark.parametrize("name", ['Ann','Jack'])
def test_5(name):
    name_test= test + ', '+ name
    assert name_test in "Good afternoon, Jack"