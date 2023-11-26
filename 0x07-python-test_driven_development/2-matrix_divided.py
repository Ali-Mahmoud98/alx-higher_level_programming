#!/usr/bin/python3

"""
Contains matrix_divided function that divides the elements of a function
by a number

"""


def matrix_divided(matrix, div):
    """
    Divides all elements of matrix

    Args:
        matrix ([[]]): list of lists of int and float
        div (int or float): a non zero number

    Returns:
        [[]]: a list of lists containing divisions made on elements
    """

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise TypeError("division by zero")

    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
