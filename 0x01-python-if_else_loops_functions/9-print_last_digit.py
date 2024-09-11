#!/usr/bin/python3

def print_last_digit(number):
    """
    Prints the last digit of a number.

    Args:
        number (int): The number to find the last digit of.

    Returns:
        int: The value of the last digit.
    """
    last_digit = abs(number) % 10  # Get the last digit using absolute value

    print("{}".format(last_digit), end="")
    return last_digit
