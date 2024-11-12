import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """ tests """
    @parameterized.expand([
        ("google", {"name": "Google", "repos_url":
                    "https://api.github.com/orgs/google/repos"}),
        ("abc", {"name": "ABC", "repos_url":
                 "https://api.github.com/orgs/abc/repos"}),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_org_data, mock_get_json):
        """tests """
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, mock_org_data)
        mock_get_json.assert_called_once_with(f"https: // api.
                                              github.com / orgs / {org_name}")
