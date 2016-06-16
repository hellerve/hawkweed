"""The IO and CachedIO monads"""
from hawkweed.functional.primitives import apply
from hawkweed.monads.monad import Monad

class IO(Monad):
    """The IO monad"""
    def __init__(self, value, *args):
        self.value = value
        self.args = args

    def ret(self):
        return apply(self.value, self.args)

    def bind(self, fun):
        return fun(apply(self.value, self.args))

class CachedIO(IO):
    """The CachedIO monad"""
    def __init__(self, value, *args):
        self.value = value
        self.args = args
        self.res = None
        self.evald = False

    def _get_cache(self):
        if self.evald:
            return self.res
        self.res = apply(self.value, self.args)
        self.evald = True
        return self.res

    def ret(self):
        return self._get_cache()

    def bind(self, fun):
        return fun(self._get_cache())
