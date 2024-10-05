#!/usr/bin/python3
"""
This module provides a function to add two integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats (casts them to integers first).

    Args:
        a: The first number (must be an integer or float).
        b: The second number, default is 98 (must be an integer or float).

    Returns:
        The integer addition of a and b after casting them to integers.

    Raises:
        TypeError: If a or b is neither an integer nor a float.

    Examples:
        >>> add_integer(1, 2)
        3
        >>> add_integer(100, -2)
        98
        >>> add_integer(2.5, 3)
        5
        >>> add_integer(10)
        108
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Cast both a and b to integers (if they are floats)
    a = int(a)
    b = int(b)

    return a + b
