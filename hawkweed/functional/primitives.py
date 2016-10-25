"""A collection of functional primitives"""
from functools import wraps, partial
from functools import reduce as _reduce
from inspect import getargspec


def curry(fun):
    """
    A working but dirty version of a currying function/decorator.
    """
    def _internal_curry(fun, original=None, given=0):
        if original is None:
            original = fun
        spec = getargspec(original)
        opt = len(spec.defaults or [])
        needed = len(spec.args) - given - opt
        @wraps(fun)
        def internal(*args, **kwargs):
            """The internal currying function"""
            if len(args) >= needed:
                return fun(*args, **kwargs)
            else:
                return _internal_curry(wraps(fun)(partial(fun, *args, **kwargs)),
                                       original,
                                       given=len(args))
        return internal
    return _internal_curry(fun)

@curry
def map(fun, values):
    """
    A function that maps a function to a list of values and returns the new generator.

    Complexity: O(n*k) where k is the complexity of the given function
    params:
        fun: the function that should be applied
        values: the list of values we should map over
    returns:
        the new generator
    """
    return (fun(value) for value in values)

@curry
def filter(fun, values):
    """
    A function that filters a list of values by a predicate function and returns
    a generator.

    Complexity: O(n*k) where k is the complexity of the given function
    params:
        fun: the fucntion that should be applied
        values: the list of values we should filter
    returns:
        the new generator
    """
    return (value for value in values if fun(value))

@curry
def reduce(fun, init, values=None):
    """
    A function that reduces a list to a single value using a given function.

    Complexity: O(n*k) where k is the complexity of the given function
    params:
        fun: the function that should be applied
        values: the list of values we should reduce
    returns:
        the reduced value
    """
    if values is None:
        return _reduce(fun, init)
    else:
        return _reduce(fun, values, init)

@curry
def apply(fun, args, kwargs=None):
    """
    applies a list of arguments (and an optional dict of keyword arguments)
    to a function.

    Complexity: O(k) where k is the complexity of the given function
    params:
        fun: the function that should be applied
        args: the list of values we should reduce
    returns:
        the reduced value
    """
    if kwargs is None:
        kwargs = {}
    return fun(*args, **kwargs)

def pipe(*funs):
    """
    composes a bunch of functions. They will be applied one after the other.

    Complexity: depends on the given functions
    params:
        *funs: the functions that should be chained
    returns: the chained function
    """
    def internal(*args, **kwargs):
        """The internal piping function"""
        return reduce(lambda acc, fun: fun(acc),
                      funs[0](*args, **kwargs),
                      funs[1:])
    return internal

def compose(*funs):
    """
    composes a bunch of functions. They will be applied in reverse order
    (so this function is the reverse of pipe).

    Complexity: depends on the given functions
    params:
        *funs: the functions that should be chained
    returns: the chained function
    """
    return apply(pipe, reversed(funs))

def starpipe(*funs):
    """
    composes a bunch of functions. They will be applied one after the other.
    The arguments will be passed as star args.

    Complexity: depends on the given functions
    params:
        *funs: the functions that should be chained
    returns: the chained function
    """
    def internal(*args, **kwargs):
        """The internal piping function"""
        return reduce(lambda acc, fun: fun(*acc),
                      funs[0](*args, **kwargs),
                      funs[1:])
    return internal

def starcompose(*funs):
    """
    composes a bunch of functions. They will be applied in reverse order
    (so this function is the reverse of starpipe). Like in starpipe, arguments
    will be passed as starargs.

    Complexity: depends on the given functions
    params:
        *funs: the functions that should be chained
    returns: the chained function
    """
    return apply(starpipe, reversed(funs))


def identity(value):
    """
    The identity function. Takes a value and returns it.

    Complexity: O(1)
    params:
        value: the value
    returns: the value
    """
    return value

@curry
def tap(fun, value):
    """
    A function that takes a function and a value, applies the function
    to the value and returns the value.

    Complexity: O(k) where k is the complexity of the given function
    params:
        fun: the function
        value: the value
    returns: the value
    """
    fun(value)
    return value

def constantly(value):
    """
    A generator that returns the given value forever.

    Complexity: O(1)
    params:
        value: the value to return
    returns: an infinite generator of the value
    """
    while True:
        yield value

def delay(fun, *args, **kwargs):
    """
    A function that takes a function and its arguments and delays its execution
    until it is needed. It also caches the executed return value and prevents
    it from being executed again (always returning the first result).

    params:
        fun: the function
        args: the function's args
        kwargs: the function's keyword arguments
    returns: the function result
    """
    # this is a horrible hack around Python 2.x's lack of nonlocal
    _int = ["__delay__unset"]
    @wraps(fun)
    def internal():
        """The internal delay function"""
        if _int[0] == "__delay__unset":
            _int[0] = fun(*args, **kwargs)
        return _int[0]
    return internal

@curry
def flip(fun, first, second, *args):
    """
    Takes a function and applies its arguments in reverse order.

    params:
        fun: the function
        first: the first argument
        second: the second argument
        args: the remaining args (this weird first, second, args thing
              is there to prevent preemptive passing of arguments)
    returns: the result of the function fun
    """
    return apply(fun, reversed(args + (first, second)))
