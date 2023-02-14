#!/usr/bin/python3
from models import base_model
"""Place file"""


class Place(base_model.BaseModel):
    """
    Place class implementing base model
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
        """ Initialize method for place"""
        super().__init__(*args, **kwargs)
