#!/usr/bin/python3
"""
Class User that inherits from BaseModel
"""
from models.base_model import BaseModel

class User(BaseModel):
    """
    The class for the users of the application
    with name, last name, password and email
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """
        Initialization of variables
        """
        super().__init__(**kwargs)
