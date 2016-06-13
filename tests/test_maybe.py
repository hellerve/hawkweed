from types import GeneratorType
from nose.tools import *
from hawkweed.functional.primitives import identity
from hawkweed.monads.maybe import *

def test_just():
    assert_equal(Just(10).bind(identity), 10)

def test_nothing():
    assert_equal(Nothing().value, None)

def test_chain():
    assert_equal(Just(10).bind(lambda val: Just(11).bind(lambda val2: val + val2)), 21)
    assert_equal(Just(10).bind(lambda val: Nothing().bind(lambda val2: val + val)), Nothing())

def test_is_just():
    assert_true(is_just(Just(1)))
    assert_false(is_just(Nothing()))

def test_is_nothing():
    assert_true(is_nothing(Nothing()))
    assert_false(is_nothing(Just(1)))

def test_is_maybe():
    assert_true(is_maybe(Just(1)))
    assert_true(is_maybe(Nothing()))
    assert_false(is_maybe(object()))

def test_from_just():
    assert_equal(from_just(Just(1)), 1)
    with assert_raises(ValueError):
        from_just(Nothing())
    with assert_raises(ValueError):
        from_just(1)

def test_from_maybe():
    assert_equal(from_maybe(Just(1), 100), 1)
    assert_equal(from_maybe(Just(1)), 1)
    assert_equal(from_maybe(Nothing(), 100), 100)
    assert_equal(from_maybe(Nothing()), None)
    with assert_raises(ValueError):
        from_maybe(1)

def test_list_to_maybe():
    assert_equal(list_to_maybe([]), Nothing())
    assert_equal(list_to_maybe([1]), Just(1))
    assert_equal(list_to_maybe([1, 10]), Just(1))
    with assert_raises(ValueError):
        list_to_maybe(1)

def test_maybe_to_list():
    assert_equal(maybe_to_list(Nothing()), [])
    assert_equal(maybe_to_list(Just(1)), [1])
    with assert_raises(ValueError):
        maybe_to_list(1)

def test_value_to_maybe():
    assert_equal(value_to_maybe([]), Nothing())
    assert_equal(value_to_maybe([1]), Just([1]))
    assert_equal(value_to_maybe(1), Just(1))
    assert_equal(value_to_maybe(0), Nothing())

def test_cat_maybe():
    assert_equal(list(cat_maybe([Just(1), Nothing(), Just(2)])),
                 [Just(1), Just(2)])

def test_map_maybe():
    assert_equal(list(map_maybe(identity, [Just(1), Nothing(), Just(2)])),
                      [Just(1), Just(2)])
    assert_is_instance(map_maybe(identity, [Just(1)]), GeneratorType)
