from nose.tools import *
from hawkweed.classes.list_cls import List

def test_repr():
    assert_equal(List([0]).__repr__(), "List([0])")

def test_str():
    x = List([0])
    assert_equal(x.__str__(), x.__repr__())
