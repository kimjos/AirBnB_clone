#!/usr/bin/python3
""" Unittest for the module Base """

import json
import unittest
from models.base_model import BaseModel
import os

class testBaseClass(unittest.TestCase):
    """ Class to rpove tests """

    def test_empty(self):
        b1 = Base()
        b2 = BAse()
        self.assertEqual(b1.id, b2.id)
