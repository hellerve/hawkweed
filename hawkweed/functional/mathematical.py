"""A few mathematical functions"""
from hawkweed.functional.primitives import curry

def inc(n):
    """
    A function that increments its argument by 1.

    Complexity: O(1)
    params:
        n: the number to increment
    returns: the incremented number
    """
    return n + 1

def dec(n):
    """
    A function that decrements its argument by 1.

    Complexity: O(1)
    params:
        n: the number to decrement
    returns: the decremented number
    """
    return n - 1

@curry
def add(x, y):
    """This is a functional wrapper around the + operator"""
    return x + y

@curry
def sub(x, y):
    """This is a functional wrapper around the - operator"""
    return x - y

@curry
def mul(x, y):
    """This is a functional wrapper around the * operator"""
    return x * y

@curry
def div(x, y):
    """This is a functional wrapper around the / operator"""
    return x / y

@curry
def mod(x, y):
    """This is a functional wrapper around the % operator"""
    return x % y

@curry
def clamp(frm, to, value):
    """
    Clamps an ordinable type between two others.

    Complexity: O(1)
    params:
        frm: the lower end
        to: the upper end
        value: the value
    returns: the clamped value
    """
    if frm > to:
        raise ValueError("frm cannot be bigger than to in clamp")
    if value > to:
        return to
    if value < frm:
        return frm
    return value
