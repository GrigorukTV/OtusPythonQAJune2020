import pytest


num_set = {1, 2, 3, 4, 5, 6}
# 1
def test_1(fixture_set):
    assert {3,2,1,3,1,3,2,2}==fixture_set

#2
@pytest.mark.parametrize('test_set',[{2,4,6}])
def test_2(test_set):
    assert {1,3,5}==num_set.difference(test_set)

#3
@pytest.mark.parametrize('issub_set',[{2,4,6}])
def test_3(issub_set):
   assert num_set.issubset(issub_set)==False

#4
@pytest.mark.parametrize('issup_set',[{1,5,6}])
def test_4(issup_set):
   assert num_set.issuperset(issup_set)==True

#5
@pytest.fixture()
def rem_set():
    num_set.remove(4)
def test_5(rem_set):
    assert 5 in num_set



