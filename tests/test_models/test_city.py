#!/usr/bin/python3
"""
Unittest for City class
"""

import json
from models.city import City
import unittest


class TestCity(unittest.TestCase):
    """
    tests for City class
    """

    def test_docstring(self):
        """
        checks if there is a docstring
        """
        self.assertIsNotNone(City.__doc__)
