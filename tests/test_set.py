from hawkweed.classes import Set
from nose.tools import *

def test_clear():
    assert_equal(Set({1,2}).clear(), Set({}))

def test_remove():
    assert_equal(Set({1}).remove(1), Set({}))

def test_add():
    assert_equal(Set({}).add(1), Set({1}))

def test_update():
    assert_equal(Set({}).update({1}), Set({1}))

def test_reset():
    reset = Set({1})
    assert_equal(Set({1, 2, 3, 4}).reset(reset), reset)

def test_remove_empty():
    assert_equal(Set({1, 2, 3, None}).remove_empty(), Set({1, 2, 3}))

def test_remove_empty_custom_fun():
    assert_equal(Set({1, 2, 3, 4}).remove_empty(fun=lambda x: x != 4), Set({1, 2, 3}))
