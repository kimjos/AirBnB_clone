#!/usrbin/python3
"""
Unittest for file storage
"""

import json
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """
    tests for User class
    """
    def test_docstring(self):
        """
        testing if there is a docstring
        """
        self.assertIsNotNone(User.__doc__)
