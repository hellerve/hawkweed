from nose.tools import *
from hawkweed.classes.future import Future
from hawkweed.functional.primitives import curry
from hawkweed.functional.mathematical import inc

def test_of_fork():
    Future.of(1).fork(curry(assert_equal)(1), None)

def test_reject():
    Future.reject(1).fork(None, curry(assert_equal)(1))

def test_encase():
    Future.encase(inc, args=(0,)).fork(curry(assert_equal)(1), None)

def test_apply():
    Future.of(1).apply(inc).fork(curry(assert_equal)(2), None)

def test_chain():
    Future.of(1).chain(Future.encase(inc)).fork(curry(assert_equal)(2), None)
