#!/usr/bin/python3
""" This Module contains a subclass 'Square' of the subclass 'Rectangle' """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ This Class is a subclass of the subclass 'Rectangle' """
    def __init__(self, size):
        super().integer_validator("size", size)
        self.__width = size
        self.__height = size

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"

    def area(self):
        """ This method returns the area of a square """
        return self.__width * self.__height
