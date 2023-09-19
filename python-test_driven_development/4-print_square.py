#!/usr/bin/python3
""" This Module contains a function that prints a square """


def print_square(size):
    """ This function prints a square of size 'size' """
    if type(size) is not int:
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')
    elif size == 0:
        return

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
