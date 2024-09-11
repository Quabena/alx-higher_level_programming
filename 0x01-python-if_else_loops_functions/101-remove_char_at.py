#!/usr/bin/python3

def remove_char_at(str, n):
    """
    Creates a copy of the string, removing the character at the position n.

    Args:
        str: The input string.
        n: The position of the character to remove (0-based index).

    Returns:
        A new string with the character at position n removed. 
        If n is out of range, the original string is returned.
    """
    if n < 0 or n >= len(str):
        return str
    
    # Construct a new string without the character at index n
    return str[:n] + str[n+1:]
