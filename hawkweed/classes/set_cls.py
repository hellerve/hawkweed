"""An augmented version of the set type."""
from hawkweed.classes.repr import Repr

class Set(Repr, set):
    """An augmented version of the set type."""
    def reset(self, other):
        """
        Resets a set to another sets content

        Complexity: O(n)
        params:
            other: the set this set should be resetted to
        returns: self
        """
        self.clear()
        self.update(other)
        return self

    def remove_empty(self, fun=None):
        """
        Removes empty elements from the list.

        Complexity: O(n+k) where k is the number of things to remove
        params:
            fun: a function that takes an element and returns whether
                 it should be kept (defaults to bool())
        returns: self
        """
        if not fun:
            fun = bool

        rem = []
        for elem in self:
            if not fun(elem):
                rem.append(elem)

        for elem in rem:
            self.remove(elem)

        return self

    def clear(self):
        """
        Augmented clear function that returns self.

        returns: self
        """
        super(Set, self).clear()
        return self

    def remove(self, *args):
        """
        Augmented remove function that returns self.

        returns: self
        """
        super(Set, self).remove(*args)
        return self

    def add(self, *args):
        """
        Augmented add function that returns self.

        returns: self
        """
        super(Set, self).add(*args)
        return self

    def update(self, *args):
        """
        Augmented update function that returns self.

        returns: self
        """
        super(Set, self).update(*args)
        return self
