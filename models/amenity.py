#!/usr/bin/python3
"""Module: amenity
This module define Amenity class

Atributes:
    name (str): name of amenity

"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """Class Amenity
    Inherits BaseModel
    create class Amenity

    Atributes:
        name (str): name of amenity

    """
    __tablename__ = "amenities"

    name = Column(String(128), nullable=False)
