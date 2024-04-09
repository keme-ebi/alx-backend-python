#!/usr/bin/env python3
"""tests the client module"""
import unittest
from client import GithubOrgClient
from parameterized import parameterized
from unittest.mock import patch


class TestGithubOrgClient(unittest.TestCase):
    """a class that inherits from unittest.TestCase in order to test
        the GithubOrgClient class
    """
    @parameterized.expand([
        ("google", {"Success": True}, "Test with google"),
        ("abc", {"Success": True}, "Test with abc")
    ])
    @patch('client.get_json')
    def test_org(self, org, expected, docstring, mocked):
        """
        a function to test GithubOrgClient.org method
        """
        mocked.return_value = expected
        test = GithubOrgClient(org)
        url = "https://api.github.com/orgs/{}".format(org)
        self.assertEqual(test.org, mocked.return_value)
        mocked.assert_called_once_with(url)
