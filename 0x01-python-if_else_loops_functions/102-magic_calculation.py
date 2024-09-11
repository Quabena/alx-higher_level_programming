#!/usr/bin/python3

def magic_calculation(a, b, c):
    """
    Performs a series of calculations based on the input values,
    following the logic of a given bytecode.

    Args:
        a: First integer
        b: Second integer
        c: Third integer

    Returns:
        The result of the calculations based on comparisons
        and arithmetic operations.
    """
    if a < b:
        return c
    if c > b:
        return a + b
    return a * b - c
