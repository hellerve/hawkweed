"""The Either monad"""
from hawkweed.monads.monad import Monad

class Either(Monad):
    """The Either abstract base class"""
    def __init__(self, value):
        raise NotImplementedError("please use the type instances Left or Right")

class Left(Either):
    """The Left instance of the Either monad"""
    def __init__(self, value):
        self.value = value

    def bind(self, fun):
        """
        The monadic bind function of Left.
        It will just return itself.

        Complexity: O(1)
        params:
            fun: the function
        returns: self
        """
        return self

class Right(Either):
    """The Right instance of the Either monad"""
    def __init__(self, value):
        self.value = value

    def bind(self, fun):
        """
        The monadic bind function of Right.
        It will just apply the function to the
        value and be done with it.

        Complexity: O(k) where k is the complexity of the function
        params:
            fun: the function
        returns: the transformed value
        """
        return fun(self.value)

def either(left, right, monad):
    """
    Takes a function left, a function right and a value
    and binds according to the value (into left if it is a Left,
    into right if it is a Right). Otherwise throws a ValueError.

    Complexity: O(1) or complexity of the given function
    params:
        left: the function that should be executed on Left
        right: the function that should be executed on Right
    throws: ValueError
    returns:
        whatever the functions return
    """
    if is_left(monad):
        return monad.bind(left)
    if is_right(monad):
        return monad.bind(right)
    raise ValueError("monad in either must either be left or right")

def lefts(monads):
    """
    Takes a list and returns only the instances of Left.

    Complexity: O(1)
    params:
        monads: the list
    returns:
        an iterable of the Left values
    """
    return (x for x in monads if is_left(x))

def rights(monads):
    """
    Takes a list and returns only the instances of Right.

    Complexity: O(1)
    params:
        monads: the list
    returns:
        a generator of the Right values
    """
    return (x for x in monads if is_right(x))

def is_either(monad):
    """
    Checks whether a value is an instance of Either.

    Complexity: O(1)
    params:
        val: the value to check
    returns: the truth value
    """
    return is_left(monad) or is_right(monad)

def is_left(monad):
    """
    Checks whether a value is an instance of Left.

    Complexity: O(1)
    params:
        val: the value to check
    returns: the truth value
    """
    return isinstance(monad, Left)

def is_right(monad):
    """
    Checks whether a value is an instance of Right.

    Complexity: O(1)
    params:
        val: the value to check
    returns: the truth value
    """
    return isinstance(monad, Right)

def partition_eithers(monads):
    """
    Takes a list and returns a two-element Atuple where the first
    element is a list of all the instances of Left and the second
    element is a list of all the instances of Right.

    Complexity: O(1)
    params:
        monads: the list of monads
    returns: the tuple
    """
    return lefts(monads), rights(monads)
