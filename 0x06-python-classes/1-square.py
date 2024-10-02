#!/usr/bin/python3
"""This module defines a class Square."""


class Square:
    """This class defines a square with a private instance attribute size."""

    def __init__(self, size):
        """Initialize the square with a given size.

        Args:
            size (int or float): The size of the square.
        """
        self.__size = size
