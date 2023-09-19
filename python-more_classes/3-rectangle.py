#!/usr/bin/python3
""" This is a module defining a Class called Rectangle """


class Rectangle:
    """ This is a Class called Rectangle """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def __str__(self):
        string_rep = ""
        for i in range(self.__height):
            for j in range(self.__width):
                string_rep += '#'
        string_rep += '\n'
        return string_rep

    @property
    def width(self):
        """ Private Attribute: Width - Getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ Private Attribute: Width - Setter """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """ Private Attribute: Height - Getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ Private Attribute: Height - Setter """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """ This method returns the area of an instance Rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ This method returns the perimeter of an instance Rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width + self.__height) * 2
