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

def and_(x, y):
    """Wraps the logical and function."""
    return x and y

def or_(x, y):
    """Wraps the logical and function."""
    return x or y

def not_(x):
    """Wraps the logical not function."""
    return not x

@curry
def complement(fun, *args, **kwargs):
    """
    Takes a function and it's args and returns it's complement.

    Complexity: O(1)
    params:
        fun: the function to complement
        *args: the arguments that should be passed to the function
        **kwaargs: the keyword arguments that should be passed to the function
    """
    return not fun(*args, **kwargs)

def false():
    """
    Always returns False.

    Complexity: O(1)
    returns: False
    """
    return False

def true():
    """
    Always returns True.

    Complexity: O(1)
    returns: True
    """
    return True
