#!/usr/bin/python3
"""This module defines a class Square.

The Square class with a size attribute and calculates its area.
"""


class Square:
    """A class that defines a square.

    Attributes:
        __size (int): The size of the square, must be a non-negative integer.
    """

    def __init__(self, size=0):
        """Initialize a new square instance.

        Args:
            size (int): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
