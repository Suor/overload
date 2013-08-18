Overload
========

Overload python functions to behave diffrently depending on number and types of arguments.


Install
-------

::

    pip install p2-overload


Usage
-----

.. code:: python

    from overload import *

    # types and number or agrs:
    @overload(int)
    def quantify(n):
        return 'quantify' * n

    @overload(str)
    def quantify(s):
        return s * 2

    @overload(str, int)
    def quantify(s, n):
        return s * n

    assert quantify(2) == 'quantifyquantify'
    assert quantify('bye') == 'byebye'
    assert quantify('xy', 3) == 'xyxyxy'

    # predicates on args
    @overload(int, int)
    def step(start, step):
        return start + step

    @overload(int, callable)
    def step(start, succ):
        return succ(start)

    # use tuple of types
    @overload((list, tuple))
    def twice(coll):
        return coll + coll

    # use custom predicates
    from whatever import _

    @overload(_ < 2) # same as lambda x: x < 2
    def fib(n):
        return n

    @overload(int)
    def fib(n):
        return fib(n-1) + fib(n-2)


TODO
----

- support named and optional arguments
- ellipsis
