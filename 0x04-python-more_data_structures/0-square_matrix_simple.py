#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    x = 0
    y = 0
    length_x = len(matrix)
    for t in matrix:
        length_y = len(t)
    result = [[0] * length_y for _ in range(length_x)]
    while x < length_x:
        while y < length_y:
            result[x][y] = matrix[x][y] ** 2
            y += 1
        x += 1
        y = 0
    return result
