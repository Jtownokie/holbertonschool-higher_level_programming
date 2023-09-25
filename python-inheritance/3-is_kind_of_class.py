#!/usr/bin/python3
""" This module contains a function
    that checks if an object is an instance of a class """


def is_kind_of_class(obj, a_class):
    """ This Function returns True if obj is an instance of a_class """
    if isinstance(obj, a_class):
        return True
    else:
        return False
