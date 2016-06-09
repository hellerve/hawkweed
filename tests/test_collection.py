from hawkweed.classes import List, Dict
from nose.tools import *

def test_get_in():
    assert_equal(List([Dict({1:1})]).get_in(0, 1), 1)

def test_get_in_not_in():
    assert_equal(List([Dict({1:1})]).get_in(1, 1), None)

def test_get_in_dflt():
    assert_equal(List([1]).get_in(1, "dflt"), "dflt")

def test_update_in():
    assert_equal(List([Dict({1:1})]).update_in(0, 1, to=2),
                 List([Dict({1:2})]))

def test_get_in_not_in():
    assert_equal(List([Dict({1:1})]).get_in(1, 1), None)

def test_get_in_dflt():
    assert_equal(List([1]).get_in(1, dflt="dflt"), "dflt")

def test_get_in_reset_dflt():
    x = List([1])
    x.DFLT = "dflt"
    assert_equal(x.get_in(1), "dflt")
