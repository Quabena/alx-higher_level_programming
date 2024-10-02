#!/usr/bin/python3
"""Magic class module."""

import math


class MagicClass:
    """A class that defines a circle."""

    def __init__(self, radius=0):
        """Initialize the MagicClass with a given radius.

        Args:
            radius: The radius of the circle.

        Raises:
            TypeError: If radius is not a number.
        """
        self.__radius = 0  # Initialize the radius
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Calculate the area of the circle.

        Returns:
            The area of the circle (π * r^2).
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculate the circumference of the circle.

        Returns:
            The circumference of the circle (2 * π * r).
        """
        return 2 * math.pi * self.__radius
