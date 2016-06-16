from hawkweed.functional.primitives import reduce
from hawkweed.classes.repr import Repr

class Future(Repr):
    def __init__(self, value):
        self.value = value
        self.transforms = []
        self.chained = []

    @staticmethod
    def of(value):
        return Future(lambda rej, res: res(value))

    @staticmethod
    def reject(value):
        return Future(lambda rej, res: rej(value))

    @staticmethod
    def encase(fun, args):
        def res(rej, res):
            try:
                return res(fun(*args))
            except Exception as e:
                return rej(e)
        return Future(res)

    def __repr__(self):
        return "Future({})".format(self.value)

    def apply(self, fun):
        self.transforms.append(fun)
        return self

    def chain(self, future):
        self.chained.append(future)
        return self

    def fork(self, res, err):
        resolver = lambda t: res(reduce(lambda acc, x: x(acc),
                                                       t,
                                                       self.transforms))
        return self.value(err, resolver)
