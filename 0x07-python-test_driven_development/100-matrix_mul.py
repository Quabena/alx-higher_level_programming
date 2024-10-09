#!/usr/bin/python3
"""
This module contains a function that multiplies 2 matrices.
"""


def matrix_mul(m_a, m_b):
    """This function multiplies two matrices.

    Args:
        m_a (list of lists of int/float): Matrix to be multiplied.
        m_b (list of lists of int/float): Matrix to be multiplied.

    Raises:
        TypeError: If m_a or m_b is not a list.
        TypeError: If m_a or m_b is not a list of lists.
        ValueError: If m_a or m_b is empty.
        TypeError: If m_a or m_b contains non-integer/float elements.
        TypeError: If rows of m_a or m_b are not of the same size.
        ValueError: If m_a and m_b cannot be multiplied.

    Returns:
        list of lists of int/float: The product of m_a and m_b.
    """

    # Validate m_a and m_b are lists
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    # Validate m_a and m_b are lists of lists
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    # Validate m_a and m_b are not empty
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    # Validate all elements in m_a and m_b are integers or floats
    if not all(isinstance
               (element, (int, float)) for row in m_a for element in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance
               (element, (int, float)) for row in m_b for element in row):
        raise TypeError("m_b should contain only integers or floats")

    # Validate all rows in m_a and m_b are of the same size
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    # Validate matrices can be multiplied
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform matrix multiplication
    result = []
    for i in range(len(m_a)):
        result_row = []
        for j in range(len(m_b[0])):
            product = 0
            for k in range(len(m_b)):
                product += m_a[i][k] * m_b[k][j]
            # Round the product to 2 decimal places
            if isinstance(product, float):
                product = round(product, 2)
            result_row.append(product)
        result.append(result_row)

    return result
