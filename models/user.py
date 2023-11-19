#!/usr/bin/python3
"""Class user that inherits from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class user.

    Attributes:
        email (str): The email user
        password (str): The password user
        first_name (str): The first_name of user
        last_name (str): The last_name of user
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
