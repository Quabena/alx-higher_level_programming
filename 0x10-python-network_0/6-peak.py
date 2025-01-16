#!/usr/bin/python3
"""
This function finds a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers.
    A peak is an element greater than or equal to its neighbors.
    """
    if not list_of_integers:
        return None

    left = 0
    right = len(list_of_integers) - 1

    while left < right:
        mid = (left + right) // 2

        # If mid is less than its right neighbor, move to the right
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            # Otherwise, stay in the left half (mid could be a peak)
            right = mid

    # At the end of the loop, left == right, which is a peak
    return list_of_integers[left]
