#!/usr/bin/python3

def uppercase(str):
    """Prints the given
    string in uppercase.

    Args:
        str: The string to convert
        to uppercase.
    """
    uppercase = ""
    
    for char in str:
        if 'a' <= char <= 'z':
            char = chr(ord(char) - 32)
        uppercase += char
    print("{}".format(uppercase))
