#!/usr/bin/python3
""" This Module contains a function that divides matrix elements """


def matrix_divided(matrix, div):
    """ This Function divides every element of a matrix by a number """
    new_matrix = []
    if matrix is None:
        raise TypeError('matrix must be a matrix (list of lists) '
                        'of integers/floats')
    if type(matrix[0]) is list:
        length = len(matrix[0])

    if (isinstance(div, (int, float)) is False
       or div != div or div == float('inf')):
        raise TypeError('div must be a number')
    elif div == 0:
        raise ZeroDivisionError('division by zero')
    elif type(matrix) is not list:
        raise TypeError('matrix must be a matrix (list of lists) '
                        'of integers/floats')
    elif all([isinstance(elem, list) for elem in matrix]) is False:
        raise TypeError('matrix must be a matrix (list of lists) '
                        'of integers/floats')
    elif all([all([isinstance(elem, (int, float)) for elem in list])
              for list in matrix]) is False:
        raise TypeError('matrix must be a matrix (list of lists) '
                        'of integers/floats')
    elif all([len(row) == length for row in matrix]) is False:
        raise TypeError('Each row of the matrix must have the same size')
    else:
        new_matrix = [[round((elem / div), 2) for elem in list]
                      for list in matrix]
        return new_matrix
