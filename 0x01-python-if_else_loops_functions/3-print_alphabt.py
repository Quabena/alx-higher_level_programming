#!/usr/bin/python3

def print_alphabet():
    """
    Prints the ASCII alphabet in lowercase, excluding 'q' and 'e'.

    Prints the letters from 'a' to 'z' except for 'q' and 'e',
    using a single print function.
    The output is not followed by a new line.
    """
    alphabet = (chr(i) for i in range(97, 123) if i != 101 and i != 113)
    print("{}".format("".join(alphabet)), end="")
