#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if any(matrix):
        for row in matrix:
            for j in range(len(row)):
                if j < len(row) - 1:
                    print("{:d}".format(row[j]), end=' ')
                else:
                    print("{:d}".format(row[j]))
    else:
        print("")
