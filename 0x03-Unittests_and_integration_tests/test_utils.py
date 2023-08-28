#!/usr/bin/env python3
"""
Testing a function from a python script
"""

from parameterized import parameterized
import unittest
from unittest.mock import Mock, patch
access_nested_map = __import__("utils").access_nested_map
get_json = __import__("utils").get_json


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


class TestGetJson(unittest.TestCase):
    """
    implements the TestGetJson.test_get_json method
    to test that utils.get_json returns the expected result.
    """
    @patch("utils.requests.get")
    def test_get_json(self, mock_requests_get):
        """
        Test the return of requests.get method
        """
        test_url_payload_pairs = [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False})
            ]
        mock_response = Mock()
        mock_response.json.return_value = test_url_payload_pairs[0][1]
        mock_requests_get.return_value = mock_response

        for test_url, test_payload in test_url_payload_pairs:
            result = get_json(test_url)

            mock_requests_get.assert_called_once_with(test_url)
            self.assertEqual(result, test_payload)


if __name__ == "__main__":
    unitest.main()
