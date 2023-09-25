#!/usr/bin/python3
""" This Module contains a Class 'Rectangle'
    that is a subclass of BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ This Class is a subclass of BaseGeometry to define a Rectangle """
    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
