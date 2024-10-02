#!/usr/bin/python3
"""This module defines a class Square.

The Square class represents a square
with a size and position attributes.
It calculates the area and can
print the square using the '#' character
with an optional position.
"""


class Square:
    """A class that defines a square.

    Attributes:
        __size (int): The size of the square,
        must be a non-negative integer.
        __position (tuple): The position of the square,
        must be a tuple of two positive integers.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square instance.

        Args:
            size (int): The size of the square. Defaults to 0.
            position (tuple): The position of
            the square as (x, y). Defaults to (0, 0).

        Raises:
            TypeError: If size is not an integer or
            position is not a tuple of two positive integers.
            ValueError: If size is less than 0 or
            position values are not positive integers.
        """
        self.size = size  # Use the setter to validate size
        self.position = position  # Use the setter to validate position

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

    @property
    def position(self):
        """tuple: The position of the square (x, y)."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square.

        Args:
            value (tuple): The position of the square.

        Raises:
            TypeError: If position is not a tuple of
            two positive integers.
            ValueError: If position values are not
            positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(pos, int) and pos >= 0 for pos in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square with the '#' character
        at the specified position.

        If size is 0, print an empty line.
        """
        if self.__size == 0:
            print("")
            return

        for _ in range(self.__position[1]):
            print("")  # Print empty lines for the vertical position

        for _ in range(self.__size):
            print(" " * self.__position[0] + '#' * self.__size)
