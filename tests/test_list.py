from dandelion.classes import List
from nose.tools import *

def test_clear():
    assert_equal(List([1,2]).clear(), List([]))

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
