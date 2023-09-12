#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = [[]]
    for iter in range(len(matrix)):
        new_matrix.append(list(map(lambda item: item ** 2, matrix[iter])))
    return new_matrix
