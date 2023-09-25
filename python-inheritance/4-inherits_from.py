#!/usr/bin/python3
""" This module contains a function
    that checks if an object is a subclass of a class """


def inherits_from(obj, a_class):
    """ This Function returns True if obj is a subclass of a_class """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
