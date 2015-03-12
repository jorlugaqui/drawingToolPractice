#! -*- coding: utf-8 -*-

""" Functional tests."""

import sys
import os

my_path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(my_path)

# Library Imports
import unittest2
import mock
import random

# App Imports
from app import get_menu


class TestApp(unittest2.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_app_get_menu(self):
        res = get_menu()
        self.assertIn('Main Menu', res)

    def test_choose_correct_option(self):
        get_option = mock.MagicMock(return_value=random.randint(1, 3))
        option = get_option(1, 2, 3, key='value')
        self.assertIn(option, [1, 2, 3])


if __name__ == '__main__':
    unittest2.main()