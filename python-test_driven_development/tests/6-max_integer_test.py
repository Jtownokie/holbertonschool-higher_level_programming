#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer
""" This module is a unittest for the function max_integer() """

class TestMaxInteger(unittest.TestCase):
    def test_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
