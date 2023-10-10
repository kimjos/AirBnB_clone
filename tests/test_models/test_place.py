#!/usr/bin/python3
"""
Unittest for Place class
"""

import json
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """
    tests for Place class
    """

    def test_docstring(self):
        """
        checks if there is a docstring
        """
        self.assertIsNotNone(Place.__doc__)
