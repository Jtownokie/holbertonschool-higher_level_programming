#!/usr/bin/python3
""" This module contains a function
    that checks if an object is a specific class """


def is_same_class(obj, a_class):
    """ This Function returns True if obj matches a_class exactly """
    if type(obj) == a_class:
        return True
    else:
        return False
