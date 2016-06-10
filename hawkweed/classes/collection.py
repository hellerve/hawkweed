"""A collection base class"""
class Collection():
    """A collection base class that introduces nested getting and setting"""

    #The default value for get_in; normally None
    DFLT = None

    def get(self, index, dflt=None):
        """This method needs to be implemented to subclass Collection"""
        raise NotImplementedError("You need to implement get to use the Collection base class")

    def __setitem__(self, *args, **kwargs):
        raise NotImplementedError("You need to implement __setitem__ to use the Collection \
                                   base class")

    def get_in(self, *keys, **kwargs):
        """
        A getter for deeply nested values.

        Complexity: the complexity differs depending on the collection's lookup/get complexity
        params:
            *keys: they keys that should be worked through
            **kwargs: this only accepts dflt (the default element, normally DFLT), all others
                      will be ignored
        returns:
            the element that was found or the default element
        """
        key = keys[0]
        cont = len(keys) > 1

        elem = self.get(key)

        if elem is None:
            return kwargs.get("dflt", self.DFLT)

        if not cont or not hasattr(elem, "get_in"):
            return elem

        return elem.get_in(*keys[1:], **kwargs)

    def update_in(self, *keys, **kwargs):
        """
        A setter for deeply nested values.

        Complexity: the complexity differs depending on the collection's lookup/set complexity
        params:
            *keys: they keys that should be worked through
            **kwargs: this only accepts to (a needed argument that specifies what the element
                      should be set to), all others will be ignored
        returns: self
        throws: Whatever a collection returns when a key does not exist (mostly Index- or KeyError)
        """
        key = keys[0]
        cont = len(keys) > 1

        elem = self.get(key)

        if cont:
            elem.update_in(*keys[1:], **kwargs)
        else:
            self[key] = kwargs["to"]
        return self
