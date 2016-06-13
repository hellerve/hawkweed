"""The Representation base class."""
class Repr(object):
    """The Representation base class."""
    def __repr__(self):
        return "{}({})".format(self.__class__.__name__, super(Repr, self).__repr__())

    def __str__(self):
        return self.__repr__()
