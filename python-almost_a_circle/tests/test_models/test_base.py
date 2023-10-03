#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
""" This is the unittest file for the 'base.py' module """


class TestBaseInit(unittest.TestCase):
    """ Test Class for Base __init__ method instantiation """


    def test_new_instance_id_none(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_new_instance_id_not_none(self):
        b1 = Base(2)
        b2 = Base(4)
        b3 = Base(30)
        self.assertEqual(b1.id, 2)
        self.assertEqual(b2.id, 4)
        self.assertEqual(b3.id, 30)

    # def test_nb_objects(self):
    #     b1 = Base()
    #     self.assertEqual(b1._Base__nb_objects, 1)

class TestToJsonString(unittest.TestCase):
    """ Test Class for Base method 'to_json_string' """

    def test_none_empty_list(self):
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_standard_use(self):
        sample_dict = [
        {'one': 1, 'two': 2, 'three': 3}, 
        {'four': 4, 'five': 5, 'six': 6}
        ]
        self.assertEqual(Base.to_json_string(sample_dict),
                        '[{"one": 1, "two": 2, "three": 3},'
                        ' {"four": 4, "five": 5, "six": 6}]')

    def test_wrong_argument_type(self):
        pass

class TestFromJsonString(unittest.TestCase):
    """ Test Class for Base method 'from_json_string' """

    def test_none_empty_string(self):
        pass

    def test_standard_use(self):
        pass

    def test_wrong_argument_type(self):
        pass

class TestSaveToFile(unittest.TestCase):
    """ Test Class for Base __init__ method instantiation """

    def test_none_as_arg(self):
        pass

    def test_standard_use(self):
        pass

    def test_wrong_argument_type(self):
        pass

    def test_file_open_fail(self):
        pass

class TestCreate(unittest.TestCase):
    """ Test Class for Base __init__ method instantiation """

    def test_standard_use(self):
        pass

    def test_wrong_argument_type(self):
        pass

class TestLoadFromFile(unittest.TestCase):
    """ Test Class for Base __init__ method instantiation """

    def test_standard_use(self):
        pass

    def test_excess_arguments(self):
        pass

    def test_file_open_fail(self):
        pass

    def test_wrong_file_contents(self):
        pass
