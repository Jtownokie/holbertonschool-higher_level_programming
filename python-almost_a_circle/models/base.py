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

    @staticmethod
    def from_json_string(json_string):
        """ This Method converts a JSON string into a list object """
        if json_string is None or json_string == '':
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """ This Method converts a list of instances into
            a JSON string and saves them to a file """
        if list_objs is None:
            with open(f"{cls.__name__}.json", "w+", encoding="utf-8") as f:
                json.dump([], f)
                return

        list_of_dicts = []
        for instance in list_objs:
            instance_dict = cls.to_dictionary(instance)
            list_of_dicts.append(instance_dict)

        json_list = Base.to_json_string(list_of_dicts)

        with open(f"{cls.__name__}.json", "w+", encoding="utf-8") as f:
            f.write(json_list)

    @classmethod
    def create(cls, **dictionary):
        """ This method returns an instance with all attributes set """
        if cls.__name__ == 'Rectangle':
            temp_instance = cls(1, 1)
        elif cls.__name__ == 'Square':
            temp_instance = cls(1)
        temp_instance.update(**dictionary)
        return temp_instance

    @classmethod
    def load_from_file(cls):
        """ This method returns a list of newly created instances """
        filename = f"{cls.__name__}.json"
        try:
            instance_list = []
            with open(filename, "r", encoding="utf-8") as f:
                json_string = f.read()
                dict_list = Base.from_json_string(json_string)
                for dict in dict_list:
                    instance_list.append(cls.create(**dict))
                return instance_list
        except Exception:
            return []
