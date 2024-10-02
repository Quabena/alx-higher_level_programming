#!/usr/bin/python3
"""My square module."""


class Square:
    """Define a Square."""

    def __init__(self, size=0):
        """Initialize the square with a given size.

        Args:
            size: The length of a side of the square.
        """
        self.size = size

    @property
    def size(self):
        """Property of the length of a side of square.

        Raises:
            TypeError: if size is not a number (float or int).
            ValueError: if size is < 0.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value: The size of the square.

        Raises:
            TypeError: if value is not a number.
            ValueError: if value < 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError('size must be a number')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Return the area of the square.

        Returns:
            The area of the square (size * size).
        """
        return self.__size * self.__size

    def __eq__(self, other):
        """Compare if two squares are equal based on their area.

        Args:
            other: Another square instance to compare.

        Returns:
            True if areas are equal, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """Compare if two squares are not equal based on their area.

        Args:
            other: Another square instance to compare.

        Returns:
            True if areas are not equal, False otherwise.
        """
        return self.area() != other.area()

    def __gt__(self, other):
        """Compare if this square is greater than another based on area.

        Args:
            other: Another square instance to compare.

        Returns:
            True if this square's area is greater, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """Compare if this square is greater than or equal to
        another based on area.

        Args:
            other: Another square instance to compare.

        Returns:
            True if this square's area is greater than or equal,
            False otherwise.
        """
        return self.area() >= other.area()

    def __lt__(self, other):
        """Compare if this square is less than another based on area.

        Args:
            other: Another square instance to compare.

        Returns:
            True if this square's area is less, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """Compare if this square is less than or equal to
        another based on area.

        Args:
            other: Another square instance to compare.

        Returns:
            True if this square's area is less than or equal,
            False otherwise.
        """
        return self.area() <= other.area()
