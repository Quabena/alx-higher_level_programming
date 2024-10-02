#!/usr/bin/python3
"""This module defines a class Square.

The class represents a square with a size attribute and calculates its area.
It can also print the square using the '#' character.
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
        self.size = size  # Use the setter to validate size

    @property
    def size(self):
        """int: The size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square with the '#' character.

        If size is 0, print an empty line.
        """
        if self.__size == 0:
            print("")
            return

        for _ in range(self.__size):
            print('#' * self.__size)
