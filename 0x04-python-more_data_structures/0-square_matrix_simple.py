#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix2 = list(map(list, matrix))
    for row in range(len(matrix2)):
        for elem in range(len(matrix2[row])):
            matrix2[row][elem] = matrix2[row][elem] * matrix2[row][elem]
    return matrix2
