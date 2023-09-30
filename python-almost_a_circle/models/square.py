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

    def update(self, *args, **kwargs):
        """ This method takes a variable
            argument list and updates attributes """
        if args:
            for arg in args:
                if arg is args[0]:
                    self.id = arg
                elif arg is args[1]:
                    self.size = arg
                elif arg is args[2]:
                    self.x = arg
                elif arg is args[3]:
                    self.y = arg
        else:
            allowed_keys = {'id', 'size', 'x', 'y'}
            for key, value in kwargs.items():
                if key in allowed_keys:
                    if key == 'id':
                        self.id = value
                    elif key == 'size':
                        self.size = value
                    elif key == 'x':
                        self.x = value
                    elif key == 'y':
                        self.y = value

    def to_dictionary(self):
        """ This method returns the attributes of an instance as a dict """
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}

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
