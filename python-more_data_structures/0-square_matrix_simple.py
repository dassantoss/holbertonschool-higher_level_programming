#!/usr/bin/python
def square_matrix_simple(matrix=[]):
    s_matrix = []
    for x in matrix:
        s_matrix.append(list(map(lambda x: x**2, x)))
    return (s_matrix)
