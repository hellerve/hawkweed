"""An Iterable baseclass"""

class Iterable():
    """An Iterable baseclass"""
    def __iter__(self):
        """This is the only functions that needs to be implemented to be an Iterable."""
        raise NotImplementedError("Iterable subclasses need to implement this function")

    def concatenate(self, *arguments):
        """
        Concatenates multiple Iterables.

        Complexity: O(1)
        params:
            *arguments: multiple Iterables
        returns: the new Iterable
        """
        def internal():
            """the internal concatenater"""
            for i in [self] + list(arguments):
                for elem in i:
                    yield elem
        return internal()

    def nth(self, num):
        """
        Returns an Iterable that will only yield every nth value.

        Complexity: O(1)
        params:
            num: the step size
        returns: the new Iterable
        """
        if num < 1:
            raise ValueError("step size must be bigger than 0, was {}".format(num))
        def internal():
            """the internal iterator"""
            for i, elem in enumerate(self):
                if i % num == 0:
                    yield elem
        return internal()
