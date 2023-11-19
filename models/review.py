#!/usr/bin/python3
"""Class review that inherit from BaseModel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Class review.

    Attributes:
        place_id (str): The id of place.
        user_id (str): The id of user.
        text (str): The text
    """
    place_id = ""
    user_id = ""
    text = ""
