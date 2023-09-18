#!/usr/bin/python3
""" This Module contains a function that divides matrix elements """


def matrix_divided(matrix, div):
    """ This Function divides every element of a matrix by a number """
    new_matrix = []
    if type(matrix[0]) is list:
        length = len(matrix[0])

    if all([isinstance(elem, list) for elem in matrix]) is False:
        raise TypeError('matrix must be a matrix (list of lists) '
                        'of integers/floats')
    elif all([all([isinstance(elem, (int, float)) for elem in list])
              for list in matrix]) is False:
        raise TypeError('matrix must be a matrix (list of lists) '
                        'of integers/floats')
    elif all([len(row) == length for row in matrix]) is False:
        raise TypeError('Each row of the matrix must have the same size')
    else:
        new_matrix = [[elem / div for elem in list] for list in matrix]
        return new_matrix
