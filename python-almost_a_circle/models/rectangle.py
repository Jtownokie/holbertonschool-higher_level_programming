#!/usr/bin/python3
""" This Module contains the Class 'Rectangle' which is a subclass of
    'Base' """
from models.base import Base


class Rectangle(Base):
    """ This Class is a subclass of 'Base' that defines attributes and
        methods of a Rectangle object """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        return (f"[{self.__class__.__name__}] ({self.id}) "
                f"{self.__x}/{self.__y} - {self.__width}/{self.__height}")

    def area(self):
        """ This method returns the area of a Rectangle object """
        return self.__width * self.__height

    def display(self):
        """ This method prints a square to stdout with # """
        for i in range(self.__y):
            print('')
        for i in range(self.__height):
            for k in range(self.__x):
                print(' ', end='')
            for j in range(self.__width):
                print('#', end='')
            print('')

    def update(self, *args):
        """ This method takes a variable
            argument list and updates attributes """
        for arg in args:
            if arg is args[0]:
                self.id = arg
            elif arg is args[1]:
                self.width = arg
            elif arg is args[2]:
                self.height = arg
            elif arg is args[3]:
                self.x = arg
            elif arg is args[4]:
                self.y = arg

    @property
    def width(self):
        """ Private Attribute '__width' Getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ Private Attribute '__width' Setter """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ Private Attribute '__height' Getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ Private Attribute '__height' Setter """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """ Private Attribute '__x' Getter """
        return self.__x

    @x.setter
    def x(self, value):
        """ Private Attribute '__x' Setter """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """ Private Attribute '__y' Getter """
        return self.__y

    @y.setter
    def y(self, value):
        """ Private Attribute '__y' Setter """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value
