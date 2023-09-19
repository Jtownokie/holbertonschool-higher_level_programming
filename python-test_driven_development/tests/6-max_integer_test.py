#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer
""" This module is a unittest for the function max_integer() """

class TestMaxInteger(unittest.TestCase):
    def test_list(self):
        self.assertEqual([1, 2, 3, 4], 4)
        self.assertEqual([1, 3, 4, 2], 4)
    
    def test_errors(self):
        self.assertRaises(TypeError, max_integer, 'hi')
