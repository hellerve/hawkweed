"""A few utility functions concerning indexable things"""
from hawkweed.functional.primitives import curry
from hawkweed.functional.mathematical import inc, dec

def first(element):
    """
    A wrapper around element[0].

    params:
        element: an element that implements __getitem__
    """
    return element[0]

def second(element):
    """
    A wrapper around element[1].

    params:
        element: an element that implements __getitem__
    """
    return element[1]

def last(element):
    """
    A wrapper around element[-1].

    params:
        element: an element that implements __getitem__
    """
    return element[-1]

@curry
def get(index, element):
    """
    A wrapper around element[index].

    params:
        index: the index at which we should get
        element: an element that implements __getitem__
    """
    return element[index]

@curry
def remove_from(index, element):
    """
    A wrapper around del element[index].

    params:
        index: the index at which we should delete
        element: an element that implements __delitem__
    """
    del element[index]
    return element

@curry
def remove_from_keep(index, element):
    """
    Non-destructively deletes the element at index index.

    Complexity: O(n)
    params:
        index: the index at which we should delete
        element: an element that implements __delitem__
    returns: the new list
    """
    return element[:index] + element[inc(index):]

@curry
def aperture(n, l):
    """
    Creates a generator of consecutive sublists of size n.
    If n is bigger than the length of the list, the
    generator will be empty.

    Complexity: O(slice_size*n)
    params:
        n: the slice size
        l: the list we should create the generator from
    returns the generator
    """
    index = 0
    stop = len(l) - dec(n)
    while index < stop:
        yield l[index:index+n]
        index += 1
