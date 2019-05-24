#!/usr/bin/python3
def matrix_divided(matrix, div):
    """function that divides all elements of a matrix.

    Args:
        matrix (int, float): list of integers or floats.
        div (int): divisor

    Returns:
        The function need to return a matrix.

    .. _PEP8:
        Style correction

    """
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if type(matrix[i][j]) != int and type(matrix[i][j]) != float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for i in matrix:
        if len(matrix[0]) != len(i):
            raise TypeError("Each row of the matrix must have the same size")
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    result = list(map(lambda i: list(map(lambda j: round((j/div), 2), i)), matrix))
    return result
