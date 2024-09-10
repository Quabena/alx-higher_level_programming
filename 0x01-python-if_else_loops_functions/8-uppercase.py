#!/usr/bin/python3

def uppercase(str):
    """Prints the given string in uppercase."""
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):
            char = chr(ord(char) - 32)
        print(char, end='')
    print()
