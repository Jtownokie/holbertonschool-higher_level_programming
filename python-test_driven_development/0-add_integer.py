#!/usr/bin/python3

def add_integer(a, b=98):
    if type(a) is not int or type(b) is not int:
        if type(a) is not float:
            raise TypeError('a must be an integer')
        elif type(b) is not float:
            raise TypeError('b must be an integer')
    return a + b
