#!/usr/bin/python3
"""Class amenity that inherit from BaseModel"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Class amenity.

    Attributes:
        name (str): The name of amenity
    """
    name = ""
