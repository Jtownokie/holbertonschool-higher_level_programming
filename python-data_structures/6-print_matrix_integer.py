#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix:
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix)):
                if j < len(matrix) - 1:
                    print("{}".format(matrix[i][j]), end=' ')
                else:
                    print("{}".format(matrix[i][j]))
