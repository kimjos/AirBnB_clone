#!/usr/bin/python3
"""
Class City that inherits from BaseModel
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Class to save the city where are the
    avaliables places to stay
    """

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialization of the city"""
        super().__init__(**kwargs)
