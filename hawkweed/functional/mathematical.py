"""A few mathematical functions"""
from hawkweed.functional.primitives import curry

def inc(num):
    """
    A function that increments its argument by 1.

    Complexity: O(1)
    params:
        num: the number to increment
    returns: the incremented number
    """
    return num + 1

def dec(num):
    """
    A function that decrements its argument by 1.

    Complexity: O(1)
    params:
        num: the number to decrement
    returns: the decremented number
    """
    return num - 1

@curry
def add(fst, snd):
    """This is a functional wrapper around the + operator"""
    return fst + snd

@curry
def sub(fst, snd):
    """This is a functional wrapper around the - operator"""
    return fst - snd

@curry
def mul(fst, snd):
    """This is a functional wrapper around the * operator"""
    return fst * snd

@curry
def div(fst, snd):
    """This is a functional wrapper around the / operator"""
    return fst / snd

@curry
def mod(fst, snd):
    """This is a functional wrapper around the % operator"""
    return fst % snd

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
