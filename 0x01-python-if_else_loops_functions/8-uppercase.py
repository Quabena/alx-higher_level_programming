#!/usr/bin/python3

def uppercase(str):
    """Prints the given string in uppercase."""
    for char in str:
        # Convert lowercase letters to uppercase
        if ord('a') <= ord(char) <= ord('z'):
            char = chr(ord(char) - 32)
        print(char, end='')
    print()  # Print newline at the end
