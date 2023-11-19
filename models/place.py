#!/usr/bin/python3
"""Class place that inherit from BaseModel"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Class place.

    Attributes:
        city_id (str): The city id.
        user_id (str): The user id.
        name (str): The name of place.
        description (str): The description of place.
        number_rooms (int): The number of rooms.
        number_bathrooms (int): The number of bathrooms.
        max_guest (int): The max of guest.
        price_by_night (int): The price by night.
        latitude (float): The latitude of place.
        longitude (float): The longitude of place.
        amenity_ids (list): The list of amenity ids.
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
