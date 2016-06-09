"""A few mathematical functions"""
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

def add(x, y):
    """This is a functional wrapper around the + operator"""
    return x + y

def sub(x, y):
    """This is a functional wrapper around the - operator"""
    return x - y

def mul(x, y):
    """This is a functional wrapper around the * operator"""
    return x * y

def div(x, y):
    """This is a functional wrapper around the / operator"""
    return x / y

def mod(x, y):
    """This is a functional wrapper around the % operator"""
    return x % y
