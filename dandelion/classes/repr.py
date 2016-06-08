class Repr():
    def __repr__(self):
        return "{}({})".format(self.__class__.__name__, super(Repr, self).__repr__())
