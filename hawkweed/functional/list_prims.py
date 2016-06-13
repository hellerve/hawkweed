"""A few utility functions concerning indexable things"""
from hawkweed.functional.primitives import curry
from hawkweed.functional.mathematical import inc

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
        element: an element that implements __delitem__
        index:
    returns: the new list
    """
    return element[:index] + element[inc(index):]
