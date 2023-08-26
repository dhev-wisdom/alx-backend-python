#!/usr/bin/env python3
"""
Testing a function from a python script
"""

from parameterized import parameterized
import unittest
access_nested_map = __import__("utils").access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    class that inherits from unittest.TestCase
    and performs unittest with @parameterized.expand decorator
    """
    @parameterized.expand([
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
            ])
    def test_access_nested_map(self, param_1, param_2, expected):
        """
        method to test that the method returns what it is supposed to.
        """
        result = access_nested_map(param_1, param_2)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ({}, ("a",), KeyError("a")),
        ({"a": 1}, ("a", "b"), KeyError("b")),
        ])
    def test_access_nested_map_exception(self, param_1, param_2, expected):
        """
        Use the assertRaises context manager to test that
        a KeyError is raised for the following inputs
        """
        with self.assertRaises(KeyError):
            result = access_nested_map(param_1, param_2)
            self.assertEqual(result, expected)


if __name__ == "__main__":
    unitest.main()
