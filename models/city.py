#!/usr/bin/python3
"""Defines the City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """Represent a city.
    Attributes:
        state_id (str): The state id.
        name (str): Name of a city.
    """

    state_id = ""
    name = ""
