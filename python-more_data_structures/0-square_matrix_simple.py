#!/usr/bin/python
def square_matrix_simple(matrix=[]):
    squared_matrix = matrix.copy()
    squared_matrix = list(map(lambda row: list(map(lambda x: x**2, row)), matrix))
    return list(squared_matrix)
