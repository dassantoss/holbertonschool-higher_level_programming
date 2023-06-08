#!/usr/bin/python
def square_matrix_simple(matrix=[]):
    s_matrix = []
    for row in matrix:
        s_matrix.append(list(map(lambda x: x**2, row)))
    return (s_matrix)
