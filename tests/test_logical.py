from nose.tools import *
from hawkweed.functional.logical import *

def test_all():
    assert_true(all(lambda x: x > 0, range(1,100)))
    assert_false(all(lambda x: x > 0, range(100,-1,-1)))

def test_any():
    assert_true(any(lambda x: x > 0, [0, 0, 0, 1, 0]))
    assert_false(any(lambda x: x > 0, [0, 0, 0, 0, -1]))

def test_complement():
    assert_false(complement(all, lambda x: x > 0, range(1, 3)))
    assert_true(complement(all, lambda x: x > 0, [0]))

def test_false():
    assert_false(false())

def test_true():
    assert_true(true())

def test_and():
    assert_true(and_(True)(True))
    assert_false(and_(False)(True))

def test_or():
    assert_true(or_(True)(True))
    assert_false(or_(False)(False))
