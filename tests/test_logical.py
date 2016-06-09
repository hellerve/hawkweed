from nose.tools import *
from hawkweed.functional.logical import *

def test_all():
    assert_true(all(lambda x: x > 0, range(1,100)))
    assert_false(all(lambda x: x > 0, range(100,-1,-1)))

def test_any():
    assert_true(any(lambda x: x > 0, [0, 0, 0, 1, 0]))
    assert_false(any(lambda x: x > 0, [0, 0, 0, 0, -1]))
