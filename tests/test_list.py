from hawkweed.classes import List
from nose.tools import *

def test_clear():
    assert_equal(List([1,2]).clear(), List([]))

def test_append():
    assert_equal(List([1,2]).append(3), List([1, 2, 3]))

def test_extend():
    assert_equal(List([1,2]).extend([3]), List([1, 2, 3]))

def test_get():
    assert_equal(List([1]).get(0), 1)

def test_get_not_in():
    assert_equal(List([1]).get(1), None)

def test_get_dflt():
    assert_equal(List([1]).get(1, "dflt"), "dflt")

def test_reset():
    reset = List([1])
    assert_equal(List([1, 2, 3, 4]).reset(reset), reset)

def test_remove_empty():
    assert_equal(List([1, 2, 3, None]).remove_empty(), List([1, 2, 3]))

def test_remove_empty_custom_fun():
    assert_equal(List([1, 2, 3, 4]).remove_empty(fun=lambda x: x != 4), List([1, 2, 3]))

def test_take():
    assert_equal(List(List(range(10)).take(5)), List(range(5)))

def test_take_iterate():
    for i, e in enumerate(List(range(10)).take(5)):
        assert_equal(i, e)

def test_drop():
    assert_equal(List(List(range(10)).drop(5)), List(range(5,10)))

def test_drop_iterate():
    dropped = 5
    for i, e in enumerate(List(range(10)).drop(dropped)):
        assert_equal(i + dropped, e)

def test_take_while():
    assert_equal(List(List(range(10)).take_while(lambda x: x < 5)), List(range(5)))

def test_take_while_iterate():
    for i, e in enumerate(List(range(10)).take_while(lambda x: x < 5)):
        assert_equal(i, e)

def test_drop_while():
    assert_equal(List(List(range(10)).drop_while(lambda x: x < 5)), List(range(5,10)))

def test_drop_while_iterate():
    dropped = 5
    for i, e in enumerate(List(range(10)).drop_while(lambda x: x < dropped)):
        assert_equal(i + dropped, e)

def test_rindex():
    assert_equal(List(range(10)).rindex(8), 1)

def test_flatten():
    assert_equal(List([[0], [1, 2], []]).flatten(), [0, 1, 2])

def test_flatten_deeply():
    assert_equal(List([[1], [2], 3, [4, [5]]]).flatten(), list(range(1, 6)))
