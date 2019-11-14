#!/usr/bin/python3
""" Unittest for the State Class """

import json
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """ Tests for State class """

    def test_docstring(self):
        """ checks in there is a docstring """
        self.assertIsNone(State.__doc__)
