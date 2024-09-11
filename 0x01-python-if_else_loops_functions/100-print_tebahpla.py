#!/usr/bin/python3

def reverse_alternate_case():
    """
    Prints the ASCII alphabet in reverse order,
    alternating lowercase and uppercase, not followed by a new line.

    Returns:
        None
    """
    for i in range(122, 96, -1):  # ASCII values for 'z' to 'a'
        # Check if the current character should be uppercase or lowercase
        if i % 2 == 0:
            print("{}".format(chr(i)), end="")  # Even index: lowercase
        else:
            print("{}".format(chr(i - 32)), end="")  # Odd index: uppercase

reverse_alternate_case()
