#!/usr/bin/python3
""" This Module contains the Class 'Rectangle' which is a subclass of
    'Base' """
from models.base import Base


class Rectangle(Base):
    """ This Class is a subclass of 'Base' that defines attributes and
        methods of a Rectangle object """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ This is the __init__ method for the Rectangle Class """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Private Attribute '__width' Getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ Private Attribute '__width' Setter """
        self.__width = value

    @property
    def height(self):
        """ Private Attribute '__height' Getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ Private Attribute '__height' Setter """
        self.__height = value

    @property
    def x(self):
        """ Private Attribute '__x' Getter """
        return self.__x

    @x.setter
    def x(self, value):
        """ Private Attribute '__x' Setter """
        self.__x = value

    @property
    def y(self):
        """ Private Attribute '__y' Getter """
        return self.__y

    @y.setter
    def y(self, value):
        """ Private Attribute '__y' Setter """
        self.__y = value
