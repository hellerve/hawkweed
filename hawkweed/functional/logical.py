"""A small collection of functions for logic."""
from hawkweed.functional.primitives import curry

@curry
def all(fun, values):
    """
    A function that will return True if the predicate is True for all
    provided values.

    Complexity: O(n)
    params:
        fun: the predicate function
        values: the values to test against
    returns: boolean
    """
    for element in values:
        if not fun(element):
            return False
    return True

@curry
def any(fun, values):
    """
    A function that will return True if the predicate is True for any
    of the provided values.

    Complexity: O(n)
    params:
        fun: the predicate function
        values: the values to test against
    returns: boolean
    """
    for element in values:
        if fun(element):
            return True
    return False
