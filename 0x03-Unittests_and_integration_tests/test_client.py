#!/usr/bin/env python3

import unittest
from unittest.mock import patch, PropertyMock, Mock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos


class TestGithubOrgClient(unittest.TestCase):
    """ tests """
    @parameterized.expand([
        ("google", {"name": "Google", "repos_url": "https://api.github.com/orgs/google/repos"}),
        ("abc", {"name": "ABC", "repos_url": "https://api.github.com/orgs/abc/repos"}),

    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_org_data, mock_get_json):
        """tests """
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, mock_org_data)
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")


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

    @patch.object(GithubOrgClient, 'get_json')
    def test_public_repos(self, mock_get_json):
        mock_repos_payload = [
            {"name": "repo1"},
            {"name": "repo2"},
        ]
        mock_get_json.return_value = mock_repos_payload
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_repos_url:
            mock_repos_url.return_value = "https://api.github.com/orgs/google/repos"
            client = GithubOrgClient("google")
            result = client.public_repos()

            self.assertEqual(result, ["repo1", "repo2"])
            mock_repos_url.assert_called_once()
            mock_get_json.assert_called_once_with("https://api.github.com/orgs/google/repos")

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected_result):
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected_result)


@parameterized_class([{"org_payload": org_payload,
                       "repos_payload": repos_payload,
                       "expected_repos": expected_repos,
                       "apache2_repos": apache2_repos}])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """tests"""
    @classmethod
    def setUpClass(cls):
        """tests"""
        cls.get_patcher = patch('requests.get')

        cls.mock_get = cls.get_patcher.start()

        def get_json_side_effect(url):
            if url == "https://api.github.com/orgs/google":
                return cls.org_payload
            elif url == "https://api.github.com/orgs/google/repos":
                return cls.repos_payload
            return None

        cls.mock_get.return_value = Mock(
            json=Mock(side_effect=get_json_side_effect))

    @classmethod
    def tearDownClass(cls):
        """Tests"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """tests"""
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """tests"""
        client = GithubOrgClient("google")
        self.assertEqual(
            client.public_repos(
                license="apache-2.0"),
            self.apache2_repos)
