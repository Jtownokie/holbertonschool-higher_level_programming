#!/usr/bin/python3
""" This Module contains the Class definition for the 'Base' Class """


class Base:
    """ This is the Base Class that defines number of objects and object id """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            __nb_objects += 1
            self.id = __nb_objects
