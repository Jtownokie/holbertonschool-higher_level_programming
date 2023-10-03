import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
""" This is the unittest file for the 'rectangle.py' module """


class TestRectangleInit(unittest.TestCase):
    """ This Test Case runs tests on the Rectangle Class' __init__ method"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_standard_use(self):
        r1 = Rectangle(1, 1)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 1)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

    def test_super_init_call(self):
        r1 = Rectangle(1, 1)
        self.assertEqual(r1.id, 1)


class TestRectangleWidth(unittest.TestCase):
    """ This Test Case runs tests on the 'Width' Attribute """

    def test_setter(self):
        r1 = Rectangle(1, 1)
        r1.width = 2
        self.assertEqual(r1.width, 2)

    def test_getter(self):
        r1 = Rectangle(1, 1)
        self.assertEqual(r1.width, 1)

    # def test_width_zero(self):
    #     with self.assertRaises(ValueError) as e:
    #         r1 = Rectangle(0, 1)

    def test_width_negative(self):
        pass

    def test_wrong_data_type(self):
        pass


class TestRectangleHeight(unittest.TestCase):
    """ This Test Case runs tests on the 'Height' Attribute """

    def test_setter(self):
        pass

    def test_getter(self):
        pass

    def test_height_zero(self):
        pass

    def test_height_negative(self):
        pass

    def test_wrong_data_type(self):
        pass


class TestRectangleX(unittest.TestCase):
    """ This Test Case runs tests on the 'X' Attribute """

    def test_setter(self):
        pass

    def test_getter(self):
        pass

    def test_x_negative(self):
        pass

    def test_wrong_data_type(self):
        pass


class TestRectangleY(unittest.TestCase):
    """ This Test Case runs tests on the 'Y' Attribute """

    def test_setter(self):
        pass

    def test_getter(self):
        pass

    def test_y_negative(self):
        pass

    def test_wrong_data_type(self):
        pass
