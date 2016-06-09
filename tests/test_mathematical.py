from nose.tools import *
from hawkweed.functional.mathematical import *

def test_inc():
    for i in range(100):
        assert_equal(inc(i), i + 1)

def test_dec():
    for i in range(100):
        assert_equal(dec(i), i - 1)
