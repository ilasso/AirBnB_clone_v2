#!/usr/bin/python3
"""Module: base city
This module defines City class

Atributes:
    state_id (str): it will be the State.id
    name (datetime): name of city
"""
from models.base_model import BaseModel


class City(BaseModel):
    """Class City
    Inherits from BaseModel
    Create class attributes by City class

    Atributes:
        state_id (str): it will be the State.id
        name (datetime): name of city

    """

    state_id = ""
    name = ""
