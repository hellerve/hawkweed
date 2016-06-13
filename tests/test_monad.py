from nose.tools import *
from hawkweed.monads.monad import Monad, doM, wrapM
from hawkweed.monads.maybe import Just

def test_doM():
    def x():
        res1 = yield Just(1)
        res2 = yield Just(2)
        yield Just(res1 + res2)
    assert_equal(doM(x()), 3)

def test_wrapM():
    assert_equal(wrapM(Just(1)).imag, 0)
    assert_equal(wrapM(Just(1)).real, 1)
    assert_equal(wrapM(Just(1)).bind(lambda x: x + 1), 2)

def test_ret():
    assert_equal(Monad(1).ret(), 1)

def test_bind_sugar():
    with assert_raises(NotImplementedError):
        Monad(1) >> 1

def test_lift():
    liftM = Monad.lift(lambda x: x)
    assert_equal(liftM(1), Monad(1))
