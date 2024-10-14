#!/usr/bin/python3
"""
    This module returns a list of all available attributes
    and methods of an object
"""


def lookup(obj):
    """This function looks for all attributes and methods of an object"""
    return dir(obj)
