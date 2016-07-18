
hawkweed
=============

Yet another implementation of missing functions.

Installation
------------

::

  pip install hawkweed

Usage
-----

hawkweed is roughly divided into three different parts: datatypes, monads and
functions. All the functions are exhaustively documented with pydoc, all the
parameters, the functions' time complexity (if applicable) and the return value
are given.

Datatypes
---------

Most of the datatypes implemented in hawkweed are mere wrappers around Python
standard datatypes. If the function does not return anything in the Python
datatype, this implementation will return ``self`` to allow for chaining.

A notable exception is the largely unstable and undocumented ``Future`` class.

.. code-block:: python

    from hawkweed import List, Dict, Set

    List([1]).append(2).extend([3, None, 4]).remove_empty() # => List([1, 2, 3, 4])
    List(range(10)).take(5) # => generator from 0 to 4
    List(range(10)).drop(5) # => generator from 5 to 9
    List(range(10)).take_while(lambda x: x < 5) # => generator from 0 to 4
    List(range(10)).drop_while(lambda x: x < 5) # => generator from 4 to 9
    List(range(10)).nth(3) # => generator yielding 0, 3, 6 and 9 (lazily); works with any subclass of Iterable
    List(range(10)).reset(range(5)) # => List([0, 1, 2, 3, 4])

    Dict({1: 2, 3: 4}).reverse() # => Dict({2: 1, 4: 3})
    Dict({1: 2, 3: 4, 2: None}).remove_empty() # => Dict({1: 2, 3: 4})
    Dict({1: 2, 3: 4, None: "go away"}).remove_empty(filter_keys=True) # => Dict({1: 2, 3: 4})
    Dict({1: 2, 3: 4, 2: 3}).remove_empty(fun=lambda x: x!=2) # => Dict({1: 2, 3: 4})
    Dict({1: 2, 3: 4}).reduce(fun=lambda acc, k, v: acc + k + v, acc=0) # => 10
    Dict({1: 2, 3: 4}).reduce(fun=lambda acc, k, v: acc + (k, v)) # => (1, 2, 3, 4)
    Dict({1: 2, 3: 4, 5: 6}).pick(1, 5) # => Dict({1: 2, 5: 6})

    Set({1, 2, 3, 4}).remove_empty(fun=lambda x: x!=3) # => Set({1, 2, 4})

    # And now for something completely different
    Dict({
      "foo": List([1, 2, 3, Dict({"bar": "baz"})])
    }).get_in("foo", 3, "bar") # => "baz"
    Dict({
      "foo": List([1, 2, 3, Dict({"bar": "baz"})])
    }).get_in("foo", 100, "bar") # => None
    Dict({
      "foo": List([1, 2, 3, Dict({"bar": "baz"})])
    }).get_in("foo", 100, "bar", dflt="i am a default value") # => "i am a default value"
    Dict({
      "foo": List([1, 2, 3, Dict({"bar": "baz"})])
    }).update_in("foo", 1, "bar", to="update") # => Dict({"foo": List([1, 2, 3, Dict({"bar": "update"})])})
    # if you want to insert your own datatype, just inherit from hawkweed.Collection
    # and implement get(key, dflt=None) and __setitem__

Functions
---------

All of the functions are standalone and curried whenever possible. They do not depend
on hawkweeds datatypes in any way.

.. code-block:: python

  from hawkweed import map, reduce, List, all, any, constantly, delay

  map(inc, range(100)) # => range(1, 101)
  incrementor = map(inc)
  incrementor(List(range(100))) # => range(1, 101)
  summator = reduce(add)
  summator(range(5)) # => 10
  all(lambda x: x > 100, [101, 102, 103]) # => True
  any(lambda x: x > 10, [3, 5, 8]) # => False
  constantly(10) # => an infinite generator of 10
  delayed = delay(print, 'Hello, World!') # => this will return a variable that, when called, will compute the result of print with the argument 'Hello, World!'
  # it will cache the result instead of recomputing it upon reevaluation, i.e. `delayed() and delayed()` will only print 'Hello, World!' once

A few other functions that you might expect from a functional programming library (``compose``,
``pipe``, ``identity``, ``apply``, ``flip``, ``curry`` and the like) are also implemented. They
should be intuitive and work as expected. If they do not or are not consider it a bug.

Monads
------

The implemented monads are: Identity, Maybe (Just/Nothing), Continuation, Either, IO, CachedIO,
and List (called ListM). do notation is also supported.

.. code-block:: python

  from hawkweed import doM, wrapM, Just

  def doMe():
    res1 = yield Just(1)
    res2 = yield Just(10)
    yield Just(res1+ res2)

  doM(doMe()) # => Just(11)
  
  wrapM(Just(10)).real
  # => 10; the wrapper will try to call the wrapped values' function whenever it does not exist in the monad

There is a callcc function and all of the functions in Haskell's Data.Maybe_ and Data.Either_ are implemented.

.. _Data.Maybe: https://hackage.haskell.org/package/base-4.9.0.0/docs/Data-Maybe.html
.. _Data.Either: https://hackage.haskell.org/package/base-4.9.0.0/docs/Data-Either.html


Have fun!
