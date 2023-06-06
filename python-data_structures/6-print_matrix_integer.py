#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None or len(matrix) == 0:
        print(" ", end="")
    else:
        for row in matrix:
            for element in row:
                print("{:d}".format(element), end="")
            print()
