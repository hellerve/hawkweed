import time
import math
from nose.tools import *
from hawkweed.functional.primitives import *
from hawkweed.functional.mathematical import add, inc

def test_curry():
    assert_equal(curry(lambda x, y: x + y)(1)(2), 3)
    assert_equal(curry(lambda x, y: x + y)(1, 2), 3)

def test_curry_decorator():
    @curry
    def add(x, y):
        return x + y
    assert_equal(add(1, 2), 3)
    assert_equal(add(1)(2), 3)
    assert_equal(add.__name__, "add")

def test_map():
    dbl = map(lambda x: x + x)
    assert_equal(list(dbl([1, 2, 3])), [2, 4, 6])

def test_reduce():
    sm = reduce(lambda acc, x: acc + x)
    assert_equal(sm([1,2,3,4]), 10)
    assert_equal(sm(10, [1,2,3,4]), 20)

def test_apply():
    sum3 = lambda x, y, z: x + y + z
    assert_equal(apply(sum3, [1, 2, 3]), sum3(1, 2, 3))
    sum3 = lambda x, y, z=0: x + y + z
    assert_equal(apply(sum3, [1, 2], {"z": 2}), sum3(1, 2, z=2))

def test_pipe():
    add1 = lambda x: x + 1
    assert_equal(pipe(add1, add1)(2), 4)
    fun1 = lambda x: x[1]
    fun2 = lambda x: x[0]
    assert_equal(pipe(fun1, fun2)([1,[4]]), 4)

def test_compose():
    add1 = lambda x: x + 1
    assert_equal(pipe(add1, add1)(2), compose(add1, add1)(2))
    fun1 = lambda x: x[1]
    fun2 = lambda x: x[0]
    assert_equal(compose(fun2, fun1)([1,[4]]), 4)

def test_identity():
    assert_equal(identity([]), [])
    assert_equal(identity(1), 1)

def test_tap():
    assert_equal(tap(identity, 1), 1)
    assert_equal(tap(identity)(1), 1)

def test_constantly():
    for i, n in enumerate(constantly(1)):
        if i > 99:
            break
        assert_equal(n, 1)

def test_delay():
    # horrible test for a horrible function, heh
    x = delay(range, 1, 10000)
    before1 = time.clock()
    x()
    after1 = time.clock()
    before2 = time.clock()
    x()
    after2 = time.clock()
    assert_true((after1 - before1) > (after2 - before2))

def test_flip():
    test = lambda x, y: [x, y]
    args = [1, 2]
    assert_equal(apply(flip(test), args), list(reversed(args)))

def test_starcompose():
    assert_equal(starcompose(add, map(inc))([1, 2]), 5)

def test_starpipe():
    assert_equal(starpipe(map(inc), add)([1, 2]), 5)
