#!/usr/bin/python3
""" This module contains a function that prints a first and last name"""


def say_my_name(first_name, last_name=""):
    """ This Function prints 'My name is <first_name> <last_name>' """
    if type(first_name) is not str:
        raise TypeError('first_name must be a string')
    elif type(last_name) is not str:
        raise TypeError('last_name must be a string')
    else:
        print(f"My name is {first_name} {last_name}")
