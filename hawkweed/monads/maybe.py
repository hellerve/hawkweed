"""The Maybe monad"""
from hawkweed.functional.list_prims import first
from hawkweed.monads.monad import Monad

class Maybe(Monad):
    """The Maybe abstract base class"""
    def __init__(self, value):
        raise NotImplementedError("please use the type instances Just or Nothing")

class Just(Maybe):
    """The Just monad"""
    def __init__(self, value):
        self.value = value

    def bind(self, fun):
        """
        The monadic bind function of Just.
        It will just apply the function to the
        value and be done with it.

        Complexity: O(k) where k is the complexity of the function
        params:
            fun: the function
        returns: the transformed value
        """
        return fun(self.value)

class Nothing(Maybe):
    """The Nothing monad"""
    def __init__(self):
        self.value = None

    def bind(self, fun):
        """
        The monadic bind function of Nothing.
        It will just return itself.

        Complexity: O(1)
        params:
            fun: the function
        returns: self
        """
        return self

def is_maybe(val):
    """
    Checks whether a value is an instance of Maybe.

    Complexity: O(1)
    params:
        val: the value to check
    returns: the truth value
    """
    return is_just(val) or is_nothing(val)

def is_just(val):
    """
    Checks whether a value is an instance of Just.

    Complexity: O(1)
    params:
        val: the value to check
    returns: the truth value
    """
    return isinstance(val, Just)

def is_nothing(val):
    """
    Checks whether a value is an instance of Nothing.

    Complexity: O(1)
    params:
        val: the value to check
    returns: the truth value
    """
    return isinstance(val, Nothing)

def from_just(val):
    """
    returns the value of a just monad; otherwise
    throws a ValueError.

    Complexity: O(1)
    params:
        val: the monad to get the value from
    throws: ValueError
    returns: the monad value
    """
    if is_just(val):
        return val.value
    raise ValueError("val is not an instance of Just")

def from_maybe(val, dflt=None):
    """
    returns the value of a maybe monad; otherwise
    throws a ValueError.
    (catamorphism function)

    Complexity: O(1)
    params:
        val: the monad to get the value from
        dflt: the default value (defaults to None)
    throws: ValueError
    returns: the monad value
    """
    if is_just(val):
        return val.value
    elif is_nothing(val):
        return dflt
    else:
        raise ValueError("val is not an instance of Maybe")

def list_to_maybe(val):
    """
    if the list is empty, return Nothing. Otherwise
    return Just with the first element of the list.

    Complexity: O(1)
    params:
        val: the list fo build a Maybe from
    throws: ValueError
    returns: the monad
    """
    if not isinstance(val, list):
        raise ValueError("val is not an instance of list")
    if val == []:
        return Nothing()
    return Just(first(val))

def maybe_to_list(val):
    """
    if the value is nothing, return an empty list.
    Otherwise return a list with the monad value
    as single element.

    Complexity: O(1)
    params:
        val: the monad to build the list from
    throws: ValueError
    returns: list
    """
    if is_nothing(val):
        return []
    elif is_just(val):
        return [val.value]
    else:
        raise ValueError("val is not an instance of Maybe")

def value_to_maybe(val):
    """
    if the value is falsy, return Nothing. Otherwise
    return Just with the value as value.

    Complexity: O(1)
    params:
        val: the value to build a Maybe from
    returns: the monad
    """
    if not val:
        return Nothing()
    return Just(val)

def cat_maybe(vals):
    """
    Takes a list of Maybes and returns a generator that produces
    all the Just values.

    Complexity: O(n)
    params:
        vals: the list of maybes
    returns:
        a generator producing all the Just values
    """
    return (val for val in vals if is_just(val))

def map_maybe(fun, vals):
    """
    Takes a function and a list of elements and maps the function
    over them. It returns a generator that produces all the values
    that are Just after applying the function.

    Complexity: O(n)
    params:
        fun: the function to apply
        vals: the list of values
    returns:
        a generator producing all the just values
    """
    for element in vals:
        processed = fun(element)
        if is_just(processed):
            yield processed
