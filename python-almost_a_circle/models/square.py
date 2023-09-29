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
