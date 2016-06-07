class List(list):
    def __repr__(self):
        return "List({})".format(super(List, self).__repr__())
