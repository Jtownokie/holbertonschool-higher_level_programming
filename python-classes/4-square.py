#!/usr/bin/python3
""" This is a class that defines a square for Classes Project Task 1"""


class Square:
    """ This is a class that defines a square for Classes Project Task 1 """
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """ Private Attribute: Self - Getter """
        return self.__size

    @size.setter
    def size(self, value):
        """ Private Attribute: Self - Setter """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """ This method returns the current square area """
        return self.__size ** 2
