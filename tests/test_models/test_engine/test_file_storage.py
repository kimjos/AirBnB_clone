#!/usr/bin/python3
""" Unittest for file storage """

import json
import unittest
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.user import User
from models.amenity import Amenity
from models.state import State


class TestFileStorage(unittest.TestCase):
    """tests for FileStorageclass"""

    def test_docstring(self):
        """ checks if there is a docstring """
        self.assertIsNotNone(FileStorage.__doc__)
