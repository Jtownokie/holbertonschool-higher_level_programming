#!/usr/bin/python3
""" This module contains a class 'Student' """


class Student:
    """ This Class defines a 'Student' with name and age """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ This method returns the attributes of a Class instance
            referred to by 'attrs' """
        new_dict = {}

        if type(attrs) is not list or attrs is None:
            return self.__dict__
        else:
            for element in attrs:
                if type(element) is not str:
                    return self.__dict__
                if element in self.__dict__.keys():
                    new_dict[element] = self.__dict__[element]

        return new_dict
