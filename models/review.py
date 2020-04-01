#!/usr/bin/python3
"""Module: review
This module defines the Review Class to AirBnB project.
Atributes:
    place_id (str): it will be the Place.id
    user_id (str): it will be the User.id
    text (str): string for data text
"""


from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class Review(BaseModel, Base):
    """Class Review
    Inherits BaseModel
    Creates class attributes for Review Class
    Atributes:
        place_id (str): it will be the Place.id
        user_id (str): it will be the User.id
        text (str): string for data text
    """

    __tablename__ = "reviews"
    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    text = Column(String(1024), nullable=False)
