from nose.tools import *
from hawkweed.functional.mathematical import *

def test_inc():
    for i in range(100):
        assert_equal(inc(i), i + 1)

def test_dec():
    for i in range(100):
        assert_equal(dec(i), i - 1)

def test_add():
    assert_equal(add(1)(2), 3)

def test_sub():
    assert_equal(sub(1)(2), -1)

def test_mul():
    assert_equal(mul(1)(2), 2)

def test_div():
    assert_equal(div(10)(10), 1)

def test_mod():
    assert_equal(mod(3)(2), 1)

def test_clamp():
    assert_equal(clamp(1, 10, 3), 3)
    assert_equal(clamp(1, 10, -3), 1)
    assert_equal(clamp(1, 10, 30), 10)
