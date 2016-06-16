from itertools import chain
from nose.tools import *
from hawkweed.monads.either import Either, Left, Right, is_right,\
        is_left, is_either, either, lefts, rights, partition_eithers
from hawkweed.functional.primitives import identity

def test_right():
    assert_equal(Right(10).bind(identity), 10)

def test_nothing():
    l = Left("failure")
    assert_equal(l.bind(lambda _: "lol"), l)

def test_is_right():
    assert_true(is_right(Right(10)))
    assert_false(is_right(Left("no")))
    assert_false(is_right(10))

def test_is_left():
    assert_true(is_left(Left("yes")))
    assert_false(is_left(Right(10)))
    assert_false(is_left(10))

def test_is_either():
    assert_true(is_either(Right(10)))
    assert_true(is_either(Left("yes")))
    assert_false(is_either(10))

def test_either():
    v = "val"
    either(lambda x: assert_equal(Left(v), x), None, Left(v))
    either(None, lambda x: assert_equal(v, x), Right(v))
    with assert_raises(ValueError):
        either(None, None, 10)

def test_lefts():
    l = [Left("failure"), Left("i died"), Left("noes")]
    lr = l + [Right(1)]
    assert_equal(list(lefts(lr)), l)

def test_rights():
    r = [Right(x) for x in range(4)]
    rl = [Left("moo")] + r
    assert_equal(list(rights(rl)), r)

def test_partition_eithers():
    r = [Right(x) for x in range(4)]
    l = [Left(x) for x in ["failure"] * 4]
    rl = list(chain.from_iterable(zip(r, l)))
    assert_equal([list(x) for x in partition_eithers(rl)], [l, r])
