"""An augmented version of the dict class"""
from hawkweed.computed import PY3
from hawkweed.classes.iterable import Iterable
from hawkweed.classes.repr import Repr
from hawkweed.classes.collection import Collection

class Dict(Repr, dict, Iterable, Collection):
    """An augmented version of the dict class"""
    def reset(self, other):
        """
        Resets a dict to another dicts content

        Complexity: O(n)
        params:
            other: the dict this dict should be resetted to
        returns: self
        """
        self.clear()
        self.update(other)
        return self

    def reverse(self):
        """
        Exchanges keys and values; if there are duplicate values, the
        last value that's been written wins.

        Complexity: O(2*n)
        returns: self
        """
        tmp = dict()
        for key, val in self.items():
            tmp[val] = key
        self.reset(tmp)
        del tmp
        return self

    def remove_empty(self, fun=None, filter_keys=False):
        """
        Removes empty pairs from the dict.

        Complexity: O(2*n)
        params:
            fun: a function that takes an element and returns whether it
                 should be kept (defaults to bool())
            filter_keys: a flag that indicates that filtering should be
                         done by keys, not by values
        returns: self
        """
        if not fun:
            fun = bool
        tmp = dict()
        for key, val in self.items():
            checker = key if filter_keys else val
            if fun(checker):
                tmp[key] = val
        self.reset(tmp)
        del tmp
        return self

    def update(self, *args, **kwargs):
        """
        Update dictionary. Same as in dict(), but returns self.

        returns: self
        """
        super(Dict, self).update(*args, **kwargs)
        return self

    def reduce(self, fun, acc=None):
        """
        Reduce the dict to a value (using function fun).

        Complexity: O(n)
        params:
            fun: a function that takes the accumulator and current key
                 and value and returns the new accumulator
            acc: the initial accumulator (defaults to tuple of first
                 key and value taken from the iterator)
        returns: self
        """
        iterator = self.items().__iter__()
        if acc is None:
            acc = iterator.__next__() if PY3 else iterator.next()
        for key, val in iterator:
            acc = fun(acc, key, val)
        return acc

    def clear(self):
        """
        Augmented clear function that returns self.

        returns: self
        """
        super(Dict, self).clear()
        return self

    def setdefault(self, *args, **kwargs):
        """
        Augmented setdefault function that returns self.

        returns: self
        """
        super(Dict, self).setdefault(*args, **kwargs)
        return self

    def pick(self, *keys):
        """
        Takes a list of keys to pick and returns a subdict that contains
        only those entries.

        Complexity: O(k) where k is the number of keys
        params:
            *keys: the keys to pick
        returns: the subdict
        """
        newd = {}

        for key in keys:
            if key in self:
                newd[key] = self[key]

        return newd
