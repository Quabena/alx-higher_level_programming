#!/usr/bin/python3
def magic_calculation(a, b):
    """Perform calculations based on the comparison of a and b.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The result of the calculation.
    """
    from magic_calculation_102 import add, sub

    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return c
    else:
        return sub(a, b)
