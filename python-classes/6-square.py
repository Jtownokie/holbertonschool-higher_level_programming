#!/usr/bin/python3
""" This is a class that defines a square for Classes Project Task 1"""


class Square:
    """ This is a class that defines a square for Classes Project Task 1 """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """ Private Attribute: Position - Getter """
        return self.__position

    @position.setter
    def position(self, value):
        """ Private Attribute: Position - Getter """
        if type(value) is not tuple:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    def area(self):
        """ This method returns the current square area """
        return self.__size ** 2

    def my_print(self):
        """ This method prints a square of size __size"""
        if self.__size == 0:
            print("")
            return
        if self.__position[1] > 0:
            y = 0
            while y < self.__position[1]:
                print("")
                y += 1

        for row in range(self.__size):
            for coord in range(self.__position[0]):
                print(" ", end="")
            for column in range(self.__size):
                print("#", end="")
            print("")
