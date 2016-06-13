"""The continuation monad"""
from hawkweed.monads.monad import Monad

class Continuation(Monad):
    """The continuation monad"""
    def __call__(self, cont):
        """
        Calls the monad with a continuation.

        Complexity: O(k) where k is the complexity of the monad value
        params:
            cont: the continuation
        returns: the result of the application
        """
        return self.value(cont)

    def bind(self, fun):
        """
        The monadic bind function of Continuation.
        Returns a function that takes a continuation.

        Complexity: O(k) where k is the complexity of the monad value
        params:
            fun: the function
        returns:
            the deferred function
        """
        return lambda cont: self.value(lambda x: fun(x)(cont))

def callcc(cc):
    """
    call with current continuation.

    Complexity: varies
    params:
        cc: the current continuation
    returns: the continuation
    """
    fun = lambda cont: cc(lambda val: Continuation(lambda _: cont(val)))(cont)
    return Continuation(fun)
