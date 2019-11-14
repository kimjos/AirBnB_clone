#!/usr/bin/python3
""" Unittest for the Review class """

import json
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """tests for Review class"""

    def test_docstring(self):
        """ checks if there is a docstring """
        self.assertIsNotNone(Review.__doc__)
