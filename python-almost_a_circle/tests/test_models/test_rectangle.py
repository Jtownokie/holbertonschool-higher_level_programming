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

    def test_width_zero(self):
        with self.assertRaises(ValueError) as e:
            r1 = Rectangle(0, 1)

    def test_width_negative(self):
        with self.assertRaises(ValueError) as e:
            r1 = Rectangle(-1, 1)

    def test_wrong_data_type(self):
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle('1', 1)
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(2.50, 1)
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle([], 1)
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle((1, 2), 1)
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(True, 1)
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(None, 1)


class TestRectangleHeight(unittest.TestCase):
    """ This Test Case runs tests on the 'Height' Attribute """

    def test_setter(self):
        r1 = Rectangle(1, 1)
        r1.height = 2
        self.assertEqual(r1.height, 2)

    def test_getter(self):
        r1 = Rectangle(1, 1)
        self.assertEqual(r1.height, 1)

    def test_height_zero(self):
        with self.assertRaises(ValueError) as e:
            r1 = Rectangle(1, 0)

    def test_height_negative(self):
        with self.assertRaises(ValueError) as e:
            r1 = Rectangle(1, -1)

    def test_wrong_data_type(self):
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(1, '1')
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(1, 2.50)
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(1, [])
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(1, (1, 2))
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(1, True)
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(1, None)

class TestRectangleX(unittest.TestCase):
    """ This Test Case runs tests on the 'X' Attribute """

    def test_setter(self):
        r1 = Rectangle(1, 1)
        r1.x = 2
        self.assertEqual(r1.x, 2)

    def test_getter(self):
        r1 = Rectangle(1, 1, 1, 1)
        self.assertEqual(r1.x, 1)

    def test_x_negative(self):
        with self.assertRaises(ValueError) as e:
            r1 = Rectangle(1, 1, -1, 1)

    def test_wrong_data_type(self):
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(1, 1, '1', 1)
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(1, 1, 2.50, 1)
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(1, 1, [], 1)
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(1, 1, (1, 2), 1)
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(1, 1, True, 1)
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(1, 1, None, 1)


class TestRectangleY(unittest.TestCase):
    """ This Test Case runs tests on the 'Y' Attribute """

    def test_setter(self):
        r1 = Rectangle(1, 1)
        r1.y = 2
        self.assertEqual(r1.y, 2)

    def test_getter(self):
        r1 = Rectangle(1, 1, 1, 1)
        self.assertEqual(r1.y, 1)

    def test_y_negative(self):
        with self.assertRaises(ValueError) as e:
            r1 = Rectangle(1, 1, 1, -1)

    def test_wrong_data_type(self):
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(1, 1, 1, '1')
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(1, 1, 1, 2.50)
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(1, 1, 1, [])
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(1, 1, 1, (1, 2))
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(1, 1, 1, True)
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(1, 1, 1, None)


class TestAreaMethod(unittest.TestCase):
    """ This test case tests the 'area' method """

    def test_standard_use(self):
        r1 = Rectangle(2, 4)
        self.assertEqual(r1.area(), 8)

    def test_incorrect_arg_num(self):
        r1 = Rectangle(2, 4)
        with self.assertRaises(TypeError) as e:
            r1.area(2)

    def test_no_instance_call(self):
        with self.assertRaises(TypeError) as e:
            Rectangle.area()


class TestDisplayMethod(unittest.TestCase):
    """ This test case tests the 'display' method """

    def test_incorrect_arg_num(self):
        r1 = Rectangle(2, 4)
        with self.assertRaises(TypeError) as e:
            r1.display(2)

    def test_no_instance_call(self):
        with self.assertRaises(TypeError) as e:
            Rectangle.display()
