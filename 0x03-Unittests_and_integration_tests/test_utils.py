#!/usr/bin/env  python3
"""
Testing a function from a python script
"""

import unittest
access_nested_map = __import__("utils").access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    class that inherits from unittest.TestCase
    and performs unittest with @parameterized.expand decorator
    """
    # @parameterized.expand
    def test_access_nested_map(self):
        """
        method to test that the method returns what it is supposed to.
        """
        self.assertEqual(access_nested_map({"a": 1}, ["a"]), 1)
        self.assertEqual(access_nested_map({"a": {"b": 2}}, ["a"]), {"b": 2})
        self.assertEqual(access_nested_map({"a": {"b": 2}}, ["a", "b"]), 2)


if __name__ == "__main__":
    unitest.main()
