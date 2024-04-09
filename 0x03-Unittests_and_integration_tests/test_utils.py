#!/usr/bin/env python3
"""unittest for utils module
"""
import unittest
from parameterized import parameterized
from utils import *
from unittest.mock import patch


class TestAccessNestedMap(unittest.TestCase):
    """a class that inherits from unittest.TestCase in order to
        test the utils.access_nested_map function
    """

    @parameterized.expand([
        ({"a":1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """tests the access_nested_map function from utils"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        with self.assertRaises(expected):
            access_nested_map(nested_map, path)

class TestGetJson(unittest.TestCase):
    """a class that inherits from unittest.Testcase in order to
        test the utils.get_json fucntion
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        with patch('utils.requests.get') as mocked:
            mocked.return_value.json.return_value = test_payload
            test = get_json(test_url)
            self.assertEqual(test, test_payload)

class TestMemoize(unittest.TestCase):
    """a class that inherits from unittest.TestCase in order to
        test the utils.memoize decorator
    """

    def test_memoize(self):
        """tests the memoize decorator"""
        class TestClass:
            
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mocked:
            call = TestClass()
            call.a_property()
            call.a_property()
            mocked.assert_called_once()
