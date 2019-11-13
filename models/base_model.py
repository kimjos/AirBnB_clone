#!/usr/bin/python3
"""This module contains tha Base model class"""
import models
import uuid
import datetime


class BaseModel():
    """Base Model class"""

    def __init__(self):
        """ init method """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def save(self):
        """saving public instance attribute"""
        self.update_at = datetime.datetime.now()

    def __str__(self):
        """Ptinting class name, id and dict"""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def to_dict(self):
        """Adding to dictionary"""
        new_dict = self.__dict__
        new_dict['created_at'] = new_dict['created_at'].isoformat()
        new_dict['updated_at'] = new_dict['updated_at'].isoformat()
        new_dict['__class__'] = self.__class__.__name__
        return new_dict
