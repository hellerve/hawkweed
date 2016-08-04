from functools import wraps
from nose.tools import assert_equal, assert_raises
from hawkweed.classes import List

def prepare(f):
    def internal():
        x = List([1,2,3,4])
        f(x)
    return internal

@prepare
def test_concatenate(x):
    y = List([5,6,7,8])
    for i, x in enumerate(x.concatenate(y)):
        assert_equal(i+1, x)

@prepare
def test_concatenate_multiple(x):
    y = List([5,6,7,8])
    z = List([9,10])
    for i, x in enumerate(x.concatenate(y, z)):
        assert_equal(i+1, x)

@prepare
def test_concatenate_none(x):
    for i, x in enumerate(x.concatenate()):
        assert_equal(i+1, x)

def test_nth():
    x = List(range(100))
    for i in x.nth(2):
        assert_equal(i % 2, 0)

def test_nth_1():
    x = List(range(100))
    for i, x in enumerate(x.nth(1)):
        assert_equal(i, x)

@prepare
def test_nth_smaller_than_0(x):
    with assert_raises(ValueError) as ve:
        x.nth(0)
    assert_equal(str(ve.exception), "step size must be bigger than 0, was 0")
    with assert_raises(ValueError) as ve:
        x.nth(-1)
    assert_equal(str(ve.exception), "step size must be bigger than 0, was -1")
