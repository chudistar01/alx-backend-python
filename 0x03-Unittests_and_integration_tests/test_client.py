#!/usr/bin/env python3

import unittest
from unittest.mock import patch, PropertyMock
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

    def test_public_repos_url(self):
        """tests"""
        mock_org_payload = {
            "repos_url": "https://api.github.com/orgs/google/repos"}

        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            mock_org.return_value = mock_org_payload
            client = GithubOrgClient("google")
            result = client._public_repos_url

            self.assertEqual(result, mock_org_payload["repos_url"])
            mock_org.assert_called_once()

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        mock_repos_payload = [
            {"name": "repo1"},
            {"name": "repo2"},
        ]
        mock_get_json.return_value = mock_repos_payload
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_repos_url:
            mock_repos_url.return_value = "http://example.com/repos"
            client = GithubOrgClient("google")
            result = client.public_repos()

            self.assertEqual(result, ["repo1", "repo2"])
            mock_repos_url.assert_called_once()
            mock_get_json.assert_called_once_with("http://example.com/repos")
