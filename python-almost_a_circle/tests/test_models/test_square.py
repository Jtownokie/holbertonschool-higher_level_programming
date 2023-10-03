import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
""" This is the unittest file for the 'square.py' module """


class TestSquareInit(unittest.TestCase):
    """ This Test Case runs tests on the Square Class' __init__ method"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_standard_use(self):
        s1 = Square(1)
        self.assertEqual(s1.width, 1)
        self.assertEqual(s1.height, 1)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)

    def test_super_init_call(self):
        s1 = Square(1)
        self.assertEqual(s1.id, 1)


class TestSquareSize(unittest.TestCase):
    """ This Test Case runs tests on the 'Size' Attribute """

    def test_setter(self):
        s1 = Square(2)
        s1.size = 2
        self.assertEqual(s1.size, 2)

    def test_getter(self):
        s1 = Square(2)
        self.assertEqual(s1.width, 2)

    def test_size_zero(self):
        with self.assertRaises(ValueError) as e:
            s1 = Square(0)

    def test_size_negative(self):
        with self.assertRaises(ValueError) as e:
            s1 = Square(-1)

    def test_wrong_data_type(self):
        with self.assertRaises(TypeError) as e:
            s1 = Square('1')
        with self.assertRaises(TypeError) as e:
            s1 = Square(2.50)
        with self.assertRaises(TypeError) as e:
            s1 = Square([])
        with self.assertRaises(TypeError) as e:
            s1 = Square((1, 2))
        with self.assertRaises(TypeError) as e:
            s1 = Square(True)
        with self.assertRaises(TypeError) as e:
            s1 = Square(None)


class TestSquareX(unittest.TestCase):
    """ This Test Case runs tests on the 'X' Attribute """

    def test_setter(self):
        s1 = Square(1, 1, 1)
        s1.x = 2
        self.assertEqual(s1.x, 2)

    def test_getter(self):
        s1 = Square(1, 1, 1)
        self.assertEqual(s1.x, 1)

    def test_x_negative(self):
        with self.assertRaises(ValueError) as e:
            s1 = Square(1, -1, 1)

    def test_wrong_data_type(self):
        with self.assertRaises(TypeError) as e:
            s1 = Square(1, '1', 1)
        with self.assertRaises(TypeError) as e:
            s1 = Square(1, 2.50, 1)
        with self.assertRaises(TypeError) as e:
            s1 = Square(1, [], 1)
        with self.assertRaises(TypeError) as e:
            s1 = Square(1, (1, 2), 1)
        with self.assertRaises(TypeError) as e:
            s1 = Square(1, True, 1)
        with self.assertRaises(TypeError) as e:
            s1 = Square(1, None, 1)


class TestSquareY(unittest.TestCase):
    """ This Test Case runs tests on the 'Y' Attribute """

    def test_setter(self):
        s1 = Square(1, 1, 1)
        s1.y = 2
        self.assertEqual(s1.y, 2)

    def test_getter(self):
        s1 = Square(1, 1, 1)
        self.assertEqual(s1.y, 1)

    def test_y_negative(self):
        with self.assertRaises(ValueError) as e:
            s1 = Square(1, 1, -1)

    def test_wrong_data_type(self):
        with self.assertRaises(TypeError) as e:
            s1 = Square(1, 1, '1')
        with self.assertRaises(TypeError) as e:
            s1 = Square(1, 1, 2.50)
        with self.assertRaises(TypeError) as e:
            s1 = Square(1, 1, [])
        with self.assertRaises(TypeError) as e:
            s1 = Square(1, 1, (1, 2))
        with self.assertRaises(TypeError) as e:
            s1 = Square(1, 1, True)
        with self.assertRaises(TypeError) as e:
            s1 = Square(1, 1, None)


class TestAreaMethod(unittest.TestCase):
    """ This test case tests the 'area' method """

    def test_standard_use(self):
        s1 = Square(4)
        self.assertEqual(s1.area(), 16)

    def test_incorrect_arg_num(self):
        s1 = Square(2)
        with self.assertRaises(TypeError) as e:
            s1.area(2)

    def test_no_instance_call(self):
        with self.assertRaises(TypeError) as e:
            Square.area()


class TestDisplayMethod(unittest.TestCase):
    """ This test case tests the 'display' method """

    def test_standard_use(self):
        s1 = Square(2, 4, 2)
        self.assertEqual(s1.display(), None)

    def test_incorrect_arg_num(self):
        s1 = Square(2, 4, 2)
        with self.assertRaises(TypeError) as e:
            s1.display(2)

    def test_no_instance_call(self):
        with self.assertRaises(TypeError) as e:
            Square.display()


class TestStrOverride(unittest.TestCase):
    """ This test case tests the '__str__' magic method """

    def test_standard_use(self):
        Base._Base__nb_objects = 0
        s1 = Square(2, 1, 3, 4)
        self.assertEqual(str(s1), '[Square] (4) 1/3 - 2')
