#!/usr/bin/python3

def lookup(obj):
    """
    Returns a list of all available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        A list containing the names of the attributes and
        methods of the object.
    """
    return dir(obj)
