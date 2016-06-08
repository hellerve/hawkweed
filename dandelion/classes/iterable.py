"""An Iterable baseclass"""
from copy import copy

from dandelion.computed import PY3

class Iterable():
    """An Iterable baseclass"""
    def __iter__(self):
        """This is the only functions that needs to be implemented to be an Iterable."""
        raise NotImplemented("Iterable subclasses need to implement this function")

    def concatenate(self, *arguments):
        """
        Concatenates multiple Iterables.

        Complexity: O(1)
        params:
            *arguments: multiple Iterables
        returns: the new Iterable
        """
        def internal():
            for i in [self] + list(arguments):
                for x in i:
                    yield x
        return internal()

    def nth(self, n):
        """
        Returns an Iterable that will only yield every nth value.

        Complexity: O(1)
        params:
            n: the step size
        returns: the new Iterable
        """
        if n < 1:
            raise ValueError("step size must be bigger than 0, was {}".format(n))
        def internal():
            for i, elem in enumerate(self):
                if i % n == 0:
                    yield elem
        return internal()
