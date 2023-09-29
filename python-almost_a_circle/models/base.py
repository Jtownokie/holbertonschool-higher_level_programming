#!/usr/bin/python3
""" This Module contains the Class definition for the 'Base' Class """
import json


class Base:
    """ This is the Base Class that defines number of objects and object id """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ This Method converts list_dictionaries into a JSON string """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
