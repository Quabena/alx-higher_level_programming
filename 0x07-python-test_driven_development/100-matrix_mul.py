#!/usr/bin/python3
"""
Matrix Operations Module.

Provides a function to multiply two matrices.
"""


def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices and returns the resulting matrix.

    Args:
        m_a (list of lists of int/float): The first matrix to multiply.
        m_b (list of lists of int/float): The second matrix to multiply.

    Raises:
        TypeError: If m_a or m_b is not a list.
        TypeError: If m_a or m_b is not a list of lists.
        ValueError: If m_a or m_b is empty.
        TypeError: If m_a or m_b contains non-integer/float elements.
        TypeError: If rows of m_a or m_b are not of the same size.
        ValueError: If m_a and m_b cannot be multiplied.

    Returns:
        list of lists of int/float: The product of m_a and m_b.

    Examples:
        >>> matrix_mul = __import__('matrix_mul').matrix_mul
        >>> m_a = [
        ...     [1, 2],
        ...     [3, 4],
        ... ]
        >>> m_b = [
        ...     [1, 2],
        ...     [2, 3],
        ... ]
        >>> print(matrix_mul(m_a, m_b))
        [[5, 8], [11, 18]]

        >>> m_a = [[1, 2]]
        >>> m_b = [
        ...     [3, 4],
        ...     [5, 6]
        ... ]
        >>> print(matrix_mul(m_a, m_b))
        [[13, 16]]

        >>> m_a = [
        ...     [1.2, 5.5, 6.2],
        ...     [4.66, 12.3, -9.2]
        ... ]
        >>> m_b = [
        ...     [5.0, 3.3],
        ...     [-2.9, 4.4],
        ...     [7.2, 4.4]
        ... ]
        >>> print(matrix_mul(m_a, m_b))
        [[34.69, 55.44], [-78.61, 29.02]]

        >>> m_a = [
        ...     [1, 2.2, 3.3, 4],
        ...     [5, 6, 7, 8.8],
        ... ]
        >>> m_b = [
        ...     [1.1, 2, 3.3],
        ...     [4.0, 5.5, 6],
        ...     [7, 8, 9],
        ...     [10.01, 11, 12.3]
        ... ]
        >>> print(matrix_mul(m_a, m_b))
        [[73.04, 84.5, 95.4], [166.59, 195.8, 223.74]]

        >>> matrix_mul()
        Traceback (most recent call last):
        TypeError: matrix_mul() missing 2 positional arguments: 'm_a' and 'm_b'

        >>> m_a = [
        ...     [1, 2],
        ...     [3, 4],
        ... ]
        >>> m_b = [
        ...     [1, 2],
        ...     [2, 3],
        ...     [4, 5]
        ... ]
        >>> print(matrix_mul(m_a, m_b))
        Traceback (most recent call last):
        ValueError: m_a and m_b can't be multiplied

        >>> print(matrix_mul([], [[1, 2]]))
        Traceback (most recent call last):
        ValueError: m_a can't be empty

        >>> print(matrix_mul([[1, 2]], [[]]))
        Traceback (most recent call last):
        ValueError: m_b can't be empty

        >>> print(matrix_mul([[]], []))
        Traceback (most recent call last):
        ValueError: m_a can't be empty

        >>> print(matrix_mul("not a list", [[1, 2]]))
        Traceback (most recent call last):
        TypeError: m_a must be a list

        >>> print(matrix_mul([[1, 2]], "also not a list"))
        Traceback (most recent call last):
        TypeError: m_b must be a list

        >>> print(matrix_mul("not a list", "also not a list"))
        Traceback (most recent call last):
        TypeError: m_a must be a list

        >>> print(matrix_mul(None, None))
        Traceback (most recent call last):
        TypeError: m_a must be a list

        >>> print(matrix_mul([1, 2], [[3, 4]]))
        Traceback (most recent call last):
        TypeError: m_a must be a list of lists

        >>> print(matrix_mul([[1, 2]], [3, 4]))
        Traceback (most recent call last):
        TypeError: m_b must be a list of lists

        >>> print(matrix_mul([1, 2], [3, 4]))
        Traceback (most recent call last):
        TypeError: m_a must be a list of lists

        >>> print(matrix_mul([[1, "non-number"]], [[3, 4]]))
        Traceback (most recent call last):
        TypeError: m_a should contain only integers or floats

        >>> print(matrix_mul([[1, 2]], [[{"a": 1}, 8.8]]))
        Traceback (most recent call last):
        TypeError: m_b should contain only integers or floats

        >>> print(matrix_mul([[1, "non-number"]], [[{"a": 1}, 8.8]]))
        Traceback (most recent call last):
        TypeError: m_a should contain only integers or floats

        >>> m_a = [
        ...     [1, 2],
        ...     [3, 4, 5]
        ... ]
        >>> m_b = [
        ...     [1, 2],
        ...     [3, 4]
        ... ]
        >>> print(matrix_mul(m_a, m_b))
        Traceback (most recent call last):
        TypeError: each row of m_a must be of the same size

        >>> m_a = [
        ...     [1, 2],
        ...     [3, 4]
        ... ]
        >>> m_b = [
        ...     [1, 2],
        ...     [3, 4, 5]
        ... ]
        >>> print(matrix_mul(m_a, m_b))
        Traceback (most recent call last):
        TypeError: each row of m_b must be of the same size

        >>> m_a = [
        ...     [1, 2],
        ...     [3, 4, 5]
        ... ]
        >>> m_b = m_a
        >>> print(matrix_mul(m_a, m_b))
        Traceback (most recent call last):
        TypeError: each row of m_a must be of the same size
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
    if not all(isinstance(element, (int, float))
               for row in m_a for element in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(element, (int, float))
               for row in m_b for element in row):
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
            result_row.append(product)
        result.append(result_row)

    return result
