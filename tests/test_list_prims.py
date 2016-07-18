from nose.tools import *
from hawkweed.functional.list_prims import *

def test_first():
    assert_equal(first([1]), 1)

def test_second():
    assert_equal(second([1, 2]), 2)

def test_last():
    assert_equal(last([1, 2, 3]), 3)

def test_get():
    assert_equal(get(2, [1, 2, 3]), 3)

def test_remove_from():
    x = [1, 2, 3]
    assert_equal(remove_from(2, x), [1, 2])
    assert_equal(x, [1, 2])

def test_remove_from_keep():
    x = [1, 2, 3]
    assert_equal(remove_from_keep(2, x), [1, 2])
    assert_equal(x, [1, 2, 3])

def test_aperture():
    x = [1, 2, 3]
    assert_equal(list(aperture(2, x)), [[1, 2], [2, 3]])

def test_aperture_empty():
    assert_equal(list(aperture(2, [])), [])

def test_aperture_bigger_n():
    assert_equal(list(aperture(2, [1])), [])
