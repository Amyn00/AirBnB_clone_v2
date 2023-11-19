#!/usr/bin/python3
"""Class state that inherit from BaseModel"""
from models.base_model import BaseModel


class State(BaseModel):
    """Class state.

    Attributes:
        name (str): The name of state.
    """
    name = ""
