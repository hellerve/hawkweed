from nose.tools import *
from hawkweed.functional.mathematical import *

def test_inc():
    for i in range(100):
        assert_equal(inc(i), i + 1)

def test_dec():
    for i in range(100):
        assert_equal(dec(i), i - 1)

def test_clamp():
    assert_equal(clamp(1, 10, 3), 3)
    assert_equal(clamp(1, 10, -3), 1)
    assert_equal(clamp(1, 10, 30), 10)
