#!/usr/bin/python3
"""
Class Amenity that inherits from BaseModel
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Class to save the Amenity
    """

    name = ""

    def __init__(self, *args, **kwargs):
        """Initialization of the amenity"""
        super().__init__(**kwargs)
