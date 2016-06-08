"""An augmented version of the list class"""
class List(list):
    """An augmented version of the list class"""
    def __repr__(self):
        """Returns a string of the form 'List(<contents>)"""
        return "List({})".format(super(List, self).__repr__())

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
            fun: a function that takes an element and returns whether it should be kept (defaults to bool())
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
        i = len(self)
        for find in reversed(self):
            i -= 1
            if elem == find:
                return i
        return -1

    def take(self, n):
        """
        A generator that returns a subarray (from 0 to n).

        Complexity: O(n+k) where k is the param
        params:
            n: the upper limit of the generator slice
        """
        for elem in self[:n]:
            yield elem

    def drop(self, n):
        """
        A generator that returns a subarray (from n to len(List)).

        Complexity: O(n+k) where k is the param
        params:
            n: the lower limit of the generator slice
        """
        for elem in self[n:]:
            yield elem

    def clear(self):
        """
        A reimplemented version of clear because it only exists in Python3.

        Complexity: O(n)
        returns: self
        """
        del self[:]
        return self
