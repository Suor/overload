from overload import *

import pytest
from whatever import _


@overload(int)
def quantify(n):
    return 'quantify' * n

@overload(str)
def quantify(s):
    return s * 2

@overload(str, int)
def quantify(s, n):
    return s * n

def test_type():
    assert quantify(2) == 'quantifyquantify'
    assert quantify('bye') == 'byebye'
    assert quantify('xy', 3) == 'xyxyxy'

    with pytest.raises(TypeError): quantify(1, 2, 3)
    with pytest.raises(TypeError): quantify([])
    with pytest.raises(TypeError): quantify('hi', 'bye')


@overload(int, int)
def step(start, step):
    return start + step

@overload(int, callable)
def step(start, succ):
    return succ(start)

def test_predicate():
    assert step(10, 3) == 13
    assert step(10, _*2) == 20


@overload((list, tuple))
def twice(coll):
    return coll + coll

@overload(int)
def twice(n):
    return int(str(n) * 2)

def test_tuple():
    assert type(twice([3, 5])) is list
    assert twice([3, 5]) == [3, 5, 3, 5]
    assert twice(3) == 33


@overload(_ < 2)
def fib(n):
    return n

@overload(int)
def fib(n):
    return fib(n-1) + fib(n-2)

def test_custom():
    assert map(fib, range(10)) == [0,1,1,2,3,5,8,13,21,34]
