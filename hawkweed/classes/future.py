"""A Future class"""
from hawkweed.functional.primitives import reduce
from hawkweed.classes.repr import Repr

class Future(Repr):
    """A Future class"""
    def __init__(self, value):
        """
        Takes a binary function (taking success and error, respectively)
        and builds a Future from it.

        Complexity: O(1)
        params:
            value: the function to encase
        returns:
            a Future
        """
        self.value = value
        self.transforms = []

    @staticmethod
    def of(value):
        """
        Creates a Future from a static value, immediately returning it.

        Complexity: O(1)
        params:
            value: the value to encase
        returns:
            a Future
        """
        return Future(lambda res, rej: res(value))

    @staticmethod
    def reject(value):
        """
        Creates a Future from a static value, immediately rejecting it.

        Complexity: O(1)
        params:
            value: the value to encase
        returns:
            a Future
        """
        return Future(lambda res, rej: rej(value))

    @staticmethod
    def encase(fun, args=None):
        """
        Encases an ordinary function in a Future. If the function runs
        as expected the return value will be returned to the success
        callback. If an exception occurs it will be returned to the
        error callback.

        Special behaviour:
        You need to specify args. If the function does not have any,
        add args=[]. If you do not a function that takes arguments
        will be returned.

        Complexity: O(1)
        params:
            fun: the function to encase
            args: the arguments to pass to the function (defaults to None,
                  override to an empty sequence if no arguments are needed)
        returns:
            a Future
        """
        if args is None:
            return lambda *args: Future.encase(fun, args=args)
        def res(res, rej):
            """Internal encase function"""
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
        """
        Chains a future to this one. This will intercept
        any calls to fork insofar as both Futures are chained
        before any call to the callbacks. Any error in both
        Futures will result in a call to the error callback.

        Complexity: O(1)
        params:
            future: the Future to chain
        returns:
            a Future
        """
        def chained(res, rej):
            """Internal chain function"""
            self.value(lambda x: future(x).fork(res, rej), rej)
        return Future(chained)

    def fork(self, res, err):
        """
        Registers resolvers for this Future.

        Complexity: O(1)
        params:
            res: the resolver function
            err: the error function
        returns:
            whatever the functions return
        """
        def resolver(trans):
            """Internal fork function that applies transformations"""
            try:
                return res(reduce(lambda acc, x: x(acc), trans, self.transforms))
            except Exception as e:
                if err:
                    return err(e)
                raise
        return self.value(resolver, err)
