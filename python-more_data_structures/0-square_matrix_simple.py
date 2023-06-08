#!/usr/bin/python
def square_matrix_simple(matrix=[]):
    s_matrix = matrix.copy()
    s_matrix = list(map(lambda row: list(map(lambda x: x**2, row)), matrix))
    return list(s_matrix)
