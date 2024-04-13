#!/usr/bin/env python3
"""tests the client module"""
import unittest
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from parameterized import parameterized, parameterized_class
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
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mocked2:
            mocked2.return_value = "random"
            test = GithubOrgClient('google')
            self.assertEqual(test.public_repos(),
                             [repo['name'] for repo in mocked.return_value])
            mocked2.assert_called_once()
            mocked.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """tests GithubOrgClient.has_license method"""
        test = GithubOrgClient('google')
        self.assertEqual(test.has_license(repo, license_key), expected)


@parameterized_class(
    ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
    [(TEST_PAYLOAD[0][0], TEST_PAYLOAD[0][1], TEST_PAYLOAD[0][2],
      TEST_PAYLOAD[0][3])]
)
class TestIntegrationGithubOrgClien(unittest.TestCase):
    """an integration class"""

    @classmethod
    def setUpClass(cls):
        """mocks requests.get to return example payloads found in fixtures"""
        cls.get_patcher = patch('utils.requests.get', side_effect=requests_get)
        cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """tears down/ stops the patcher"""
        cls.get_patcher.stop()
