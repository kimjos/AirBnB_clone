#!/usr/bin/python3
""" Unittest for Base Model class """

import json
import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """tests for the Base Model class"""

    def test_docstring(self):
        """ checks if there is a docstring """
        self.assertIsNotNone(BaseModel.__doc__)
