#!/usr/bin/python3

def reverse_alternate_case():
    """
    Prints the ASCII alphabet in reverse order,
    alternating lowercase and uppercase, not followed by a new line.

    Returns:
        None
    """
    # Initialize the starting ASCII value for 'z'
    for i in range(122, 96, -1):  # ASCII values for 'z' to 'a'
        # Print lowercase for even values and uppercase for odd values
        print("{}".format(chr(i) if i % 2 == 0 else chr(i - 32)), end="")
