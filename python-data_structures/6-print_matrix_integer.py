#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None or len(matrix) == 0:
        print(" ", end="")
    else:
        for row in matrix:
            print(' '.join('{:d}'.format(element) for element in row))
