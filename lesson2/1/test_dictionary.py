import pytest


people = {'Alice': {'phone': '2341', 'addr': 'Foo drive 23'},
          'Beth':  {'phone': '9102', 'addr': 'Bar street 42'}
          }

people_2= {'Alice': {'phone': '2341', 'addr': 'Foo drive 23'},
          'Beth':  {'phone': '9102', 'addr': 'Bar street 42'}
          }


#1
def test_1(fixture_dict):
    fixture_dict.clear()
    assert fixture_dict=={}

#2
@pytest.mark.parametrize('add_dict',[2])
def test_2(add_dict,fixture_dict):
    fixture_dict.update({'ten':10,
                         'hundred':100,
                         'thousand':1000
                         })
    assert 2220==sum(fixture_dict.values())*add_dict

#3
@pytest.mark.parametrize('name',['Alice'])
def test_3(name):
   assert name in people.keys()

#4
def test_4():
   assert people==people_2

#5
def test_5(fixture_dict):
    fixture_dict.update({"b":2,
                         "a":1,
                         "d":4,
                         "c":3
                         })
    sort_dict = list(fixture_dict.keys())
    sort_dict.sort()
    assert fixture_dict=={"a":1,
                          "b":2,
                          "c":3,
                          "d":4
                          }