"""An augmented version of the list class"""
from hawkweed.classes.iterable import Iterable
from hawkweed.classes.repr import Repr
from hawkweed.classes.collection import Collection

class List(Repr, list, Iterable, Collection):
    """An augmented version of the list class"""
    def reset(self, other):
        """
        Resets a list to another lists content

        Complexity: O(n+m)
        params:
            other: the list this list should be resetted to
        returns: self
        """
        self.clear()
        self.extend(other)
        return self

    def remove_empty(self, fun=None):
        """
        Removes empty elements from the list.

        Complexity: O(3*n)
        params:
            fun: a function that takes an element and returns whether it
                 should be kept (defaults to bool())
        returns: self
        """
        if not fun:
            fun = bool

        tmp = []
        for elem in self:
            if fun(elem):
                tmp.append(elem)

        self.reset(tmp)
        del tmp
        return self

    def rindex(self, elem):
        """
        Gets the index of an element starting from the end. Does not copy the list.

        Complexity: O(n)
        params:
            elem: the element that should be found
        returns: self
        """
        for i, find in enumerate(reversed(self)):
            if elem == find:
                return i
        return -1

    def take(self, num):
        """
        A generator that returns a subarray (from 0 to num).

        Complexity: O(n+k) where k is the param
        params:
            num: the upper limit of the generator slice
        """
        for i, elem in enumerate(self):
            if num <= i:
                break
            yield elem

    def take_while(self, fun):
        """
        A generator that returns elements while a given function fun returns True.

        Complexity: O(n)
        params:
            fun: the predicate function
        """
        for elem in self:
            if fun(elem):
                yield elem
            else:
                break

    def drop(self, num):
        """
        A generator that returns a subarray (from num to len(List)).

        Complexity: O(n+k) where k is the param
        params:
            num: the lower limit of the generator slice
        """
        for elem in self[num:]:
            yield elem

    def drop_while(self, fun):
        """
        A generator that skips elements while a given function fun returns True.

        Complexity: O(n+k)
        params:
            fun: the predicate function
        """
        i = 0
        for i, elem in enumerate(self):
            if not fun(elem):
                break

        for elem in self[i:]:
            yield elem

    def clear(self):
        """
        A reimplemented version of clear because it only exists in Python3.

        Complexity: O(n)
        returns: self
        """
        del self[:]
        return self

    def append(self, *args, **kwargs):
        """
        Augmented update function that returns self.

        returns: self
        """
        super(List, self).append(*args, **kwargs)
        return self

    def extend(self, *args, **kwargs):
        """
        Augmented extend function that returns self.

        returns: self
        """
        super(List, self).extend(*args, **kwargs)
        return self

    def get(self, index, dflt=None):
        """
        A getter function that behaves like dict.get.

        params:
            index: the index to get
            dflt: the default return value (defaults to None)
        returns: self
        """
        if len(self) > index:
            return self[index]
        return dflt

    def flatten(self):
        """
        Returns a new deeply flattened list.

        Complexity: O(n)
        returns: the flattened list
        """
        flattened = []
        for item in self:
            if isinstance(item, List):
                flattened.extend(item.flatten())
            elif isinstance(item, list):
                flattened.extend(List(item).flatten())
            else:
                flattened.append(item)
        return flattened
