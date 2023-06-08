#!/usr/bin/python
def square_matrix_simple(matrix=[]):
    new_matrix = [[element**2 for element in row] for row in matrix]
    return new_matrix
