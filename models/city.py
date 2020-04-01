#!/usr/bin/python3
"""Module: base city
This module defines City class
Atributes:
    state_id (str): it will be the State.id
    name (datetime): name of city
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.place import Place


class City(BaseModel, Base):
    """Class City
    Inherits BaseModel
    Create class attributes by City class
    Atributes:
        state_id (str): it will be the State.id
        name (datetime): name of city
    """
    __tablename__ = 'cities'

    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    places = relationship("Place", backref="cities", cascade="all, delete")
