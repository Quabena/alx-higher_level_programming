#!/usr/bin/python3

def uppercase(str):
    """
    Prints a string in uppercase.

    Args:
        str (str): The string to convert to uppercase.
    """
    result = ""

    for char in str:
        # Convert lowercase letters to uppercase
        if 'a' <= char <= 'z':
            char = chr(ord(char) - 32)
        result += char

    print("{}".format(result))
