from nose.tools import *
from hawkweed.functional.primitives import identity
from hawkweed.monads.listm import ListM

def test_unit():
    x = ListM.unit(1)
    assert_equal(next(x), 1)
    with assert_raises(StopIteration):
        next(x)

def test_bind():
    x = ListM(range(10))
    for i, x in enumerate(x.bind(identity)):
        assert_equal(i, x)
