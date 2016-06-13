"""The identity monad"""
from hawkweed.monads.monad import Monad

class Identity(Monad):
    """The identity monad"""
    def bind(self, fun):
        """
        The monadic bind function of Identity.
        It will just apply the function to the
        value and be done with it.

        Complexity: O(k) where k is the complexity of the function
        params:
            fun: the function
        returns: the transformed value
        """
        return fun(self.value)
