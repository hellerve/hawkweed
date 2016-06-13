from hawkweed.classes import Dict
from nose.tools import *

def test_reverse():
    assert_equal(Dict({1: 2, 3: 4}).reverse(), Dict({2: 1, 4: 3}))

def test_reset():
    reset = Dict({2: 1, 4: 3})
    assert_equal(Dict({1: 2, 3: 4}).reset(reset), reset)

def test_clear():
    assert_equal(Dict({1: 2, 3: 4}).clear(), Dict({}))

def test_setdefault():
    d = Dict({2: 1, 4: 3})
    assert_equal(d.setdefault(1), d)

def test_update():
    assert_equal(Dict({1: 2, 3: 4}).update({2: 3}), Dict({1: 2, 2: 3, 3: 4}))

def test_remove_empty():
    assert_equal(Dict({1: 2, 3: None}).remove_empty(), Dict({1: 2}))

def test_remove_empty_keys():
    assert_equal(Dict({1: 2, None: 3}).remove_empty(filter_keys=True), Dict({1: 2}))

def test_remove_empty_custom_fun():
    assert_equal(Dict({1: 2, 4: 3}).remove_empty(fun=lambda x: x != 3), Dict({1: 2}))

def test_reduce():
    assert_equal(Dict({1: 2, 3: 4}).reduce(lambda acc, k, v: acc + k + v, 0), 10)

def test_reduce_no_acc():
    assert_equal(Dict({1: 2, 3: 4}).reduce(lambda acc, k, v: acc + (k, v)), (1, 2, 3, 4))

def test_pick():
    d = Dict({1: 2, 3: 4, 5: 6})
    assert_equal(d.pick(1, 5), Dict({1: 2, 5: 6}))
