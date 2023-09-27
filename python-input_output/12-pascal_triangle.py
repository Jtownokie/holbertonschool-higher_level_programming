#!/usr/bin/python3
""" This module contains a technical interview response that returns a
    representation of Pascal's Triangle """


def pascal_triangle(n):
    """ This function returns a list of lists of integers representing
        the Pascal's triangle of 'n' """
    if n <= 0:
        return []
    else:
        pascal_list = []

        for i in range(1, n + 1):
            current_elem = 1
            row_list = []
            for j in range(1, i + 1):
                row_list.append(current_elem)
                current_elem = current_elem * (i - j) // j
            pascal_list.append(row_list)
    return pascal_list
