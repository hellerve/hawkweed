from nose.tools import *
from hawkweed.monads.identity import Identity

def test_identity():
    assert_equal(Identity(1).value, 1)
    assert_equal(Identity(1).bind(lambda x: x + 1), 2)
