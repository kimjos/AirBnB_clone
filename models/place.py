#!/usr/bin/python3
"""
Class Place that inherits from BaseModel
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Class place that describes the place
    where people are going to stay
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """Initialization of the place"""
        super().__init__(**kwargs)
