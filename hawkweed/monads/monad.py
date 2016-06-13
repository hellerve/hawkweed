"""The monad base class"""
from hawkweed.functional.primitives import apply

class Monad(object):
    """The monad base class"""
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return "{}({})".format(self.__class__.__name__, self.value)

    def __str__(self):
        return self.__repr__

    def ret(self):
        """
        Returns the monad value.

        Complexity: O(1)
        returns: the monads value
        """
        return self.value

    def bind(self, fun):
        """
        The bind function. Needs to be implemented by any monad.

        Complexity: varies
        params:
            fun: the function to bind ti the monad value
        returns:
            the manipulated monad value
        """
        raise NotImplementedError("Monads need to implement the bind function")

    def __rshift__(self, val):
        """
        The 'bind' operator. Syntactic sugar for binding.
        """
        return self.bind(val)

    @classmethod
    def lift(cls, fun):
        """
        Lifts a function into the monad.

        Complexity: O(1)
        params:
            fun: the function to lift
        returns: a function that funnels values into the given
                 function and returns the result wrapped in a monad
        """
        def lifter(*args, **kwargs):
            "The lifting function"""
            return cls(apply(fun, args, kwargs))
        return lifter

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.value == other.value

    def __ne__(self, other):
        return not self.__eq__(other)

def doM(fun):
    """
    Takes a generator and unpacks values for every yield.

    Complexity: O(k) where k is the complexity of fun
    params:
        fun: the generator
    returns: the return value of the generator
    """
    def internal(value):
        """The step function"""
        try:
            res = fun.send(value).value
            return internal(res)
        except StopIteration:
            return value
    return internal(next(fun).value)

def wrapM(monad):
    """
    Takes a monad and wraps it so that any attribute that is not
    in the monad is automaticall forwarded to the monad value.

    Complexity: O(1)
    params:
        monad: the monad to wrap
    returns: the proxy object
    """
    class Proxy():
        """The monad proxy object"""
        def __init__(self, monad):
            self.monad = monad

        def __getattr__(self, prop):
            if hasattr(self.monad, prop):
                return getattr(self.monad, prop)
            elif hasattr(self.monad.value, prop):
                return getattr(self.monad.value, prop)
            raise AttributeError(prop)

    return Proxy(monad)
