#!/usr/bin/python3
"""This module inherits from the built in list class"""


class MyList(list):
    """A class that inherits from list"""
    def print_sorted(self):
        """prints elements of a sorted list"""
        print(sorted(self))
