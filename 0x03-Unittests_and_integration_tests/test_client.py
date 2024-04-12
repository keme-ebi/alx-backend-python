#!/usr/bin/env python3
"""tests the client module"""
import unittest
from client import GithubOrgClient
from parameterized import parameterized
from unittest.mock import patch, PropertyMock


class TestGithubOrgClient(unittest.TestCase):
    """a class that inherits from unittest.TestCase in order to test
        the GithubOrgClient class
    """

    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch('client.get_json', return_value={"payload": True})
    def test_org(self, org, mocked):
        """tests the GithubOrgClient.org method"""
        test = GithubOrgClient(org)
        url = "https://api.github.com/orgs/{}".format(org)
        self.assertEqual(test.org, mocked.return_value)
        mocked.assert_called_once_with(url)

    def test_public_repos_url(self):
        """tests the _public_repos_url method"""
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mocked:
            mocked.return_value = {"repos_url": "http://example.com"}
            test = GithubOrgClient('google')
            self.assertEqual(test._public_repos_url,
                             mocked.return_value.get('repos_url'))

    @patch("client.get_json", return_value=[{"name": "l1"}, {"name": "l2"}])
    def test_public_repos(self, mocked):
        """test the GithubOrgClient.public_repos mehtod"""
        url = "https://api.github.com/orgs/google"
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mocked2:
            mocked2.return_value = url
            test = GithubOrgClient('test')
            self.assertEqual(test.public_repos(),
                             [repo['name'] for repo in mocked.return_value])
            mocked2.assert_called_once()
            mocked.assert_called_once()
