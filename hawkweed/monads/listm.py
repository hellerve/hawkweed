"""The list monad"""
from hawkweed.monads.monad import Monad

class ListM(Monad):
    """The list monad"""

    @staticmethod
    def unit(val):
        """
        takes one value and returns a generator that yields that value.

        Complexity: O(1)
        params:
            val: the value to yield
        returns:
            the generator of the parameter
        """
        yield val

    def bind(self, fun):
        """
        The monadic bind function of ListM.
        It will apply the function to all the elements of the
        value and return a generator.

        Complexity: O(k*n) where k is the complexity of the function
        params:
            fun: the function
        returns:
            the generator of the transformed values
        """
        for element in self.value:
            yield fun(element)
