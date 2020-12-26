#!/usr/bin/env python

"""Tests for `django_social_oauth_two_factor` package."""


import unittest
from click.testing import CliRunner

from django_social_oauth_two_factor import django_social_oauth_two_factor
from django_social_oauth_two_factor import cli


class TestDjango_social_oauth_two_factor(unittest.TestCase):
    """Tests for `django_social_oauth_two_factor` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'django_social_oauth_two_factor.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
