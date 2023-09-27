#!/usr/bin/python3
""" This module contains a function that
    prepares a class instance for JSON serialization"""


def class_to_json(obj):
    """ This module returns the __dict__ of a class instance """
    return obj.__dict__
