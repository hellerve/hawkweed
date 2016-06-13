from nose.tools import *
from hawkweed.monads.continuation import Continuation, callcc

def test_call():
    assert_equal(Continuation(lambda x: x + 10)(10), 20)

def test_bind():
    assert_equal(Continuation(lambda x: x)(lambda x: x + 10)(10), 20)

def test_callcc():
    assert_equal(callcc(lambda x: x)(lambda x: x)(10)(20), 20)
