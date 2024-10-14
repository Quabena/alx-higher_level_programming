#!/usr/bin/python3
"""Checks if the object is exactly an instance of a class"""


def is_same_class(obj, a_class):
    """Return true if the object is exactly an instance of the
    class, otherwise return false
    """
    return (type(obj) == a_class)
