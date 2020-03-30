#!/usr/bin/python3
"""Module: review
This module defines the Review Class to AirBnB project.

Atributes:
    place_id (str): it will be the Place.id
    user_id (str): it will be the User.id
    text (str): string for data text

"""


from models.base_model import BaseModel


class Review(BaseModel):
    """Class Review
    Inherits from BaseModel
    Creates class attributes for Review Class

    Atributes:
        place_id (str): it will be the Place.id
        user_id (str): it will be the User.id
        text (str): string for data text

    """

    place_id = ""
    user_id = ""
    text = ""
