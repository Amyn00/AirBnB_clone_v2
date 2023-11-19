#!/usr/bin/python3
"""Class city that inherit from BaseModel"""
from models.base_model import BaseModel


class City(BaseModel):
    """Class city.

    Attributes:
        state_id (str): The id of the State
        name (str): The name of city
    """
    state_id = ""
    name = ""
