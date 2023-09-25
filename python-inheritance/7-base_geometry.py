#!/usr/bin/python3
""" This module contains a Class 'BaseGeometry' """


class BaseGeometry:
    """ This is the BaseGeomety Class """
    def area(self):
        """ This is a placeholder method """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """ This method validates an integer value """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        else:
            return
