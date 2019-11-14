#!/usr/bin/python3
""" Unittest for Amenity class """

import json
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """ tests for Amenity class """
    def test_docstring(self):
        """  checks if there is a docstring """
        self.assertIsNotNone(Amenity.__doc__)
