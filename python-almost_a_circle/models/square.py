#!/usr/bin/python3
""" This Module contains the Class 'Square' which is a subclass of
    'Rectangle' """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ This is a subclass of Rectangle with
        unique constructor attribute 'size' """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return (f"[{self.__class__.__name__}] ({self.id}) "
                f"{self.x}/{self.y} - {self.width}")

    @property
    def size(self):
        """ Private Attribute '__width' Getter """
        return self.width

    @size.setter
    def size(self, value):
        """ Private Attributes '__width' & '__height' Setter """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = value
            self.height = value
