#!/usr/bin/python3
"""Module: state
This module defines the State Class to AirBnB project.

Atributes:
    name (str): name of state

"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
import models
import os


class State(BaseModel, Base):
    """Class State
    Inherits from BaseModel
    Creates class attributes for State Class

    Atributes:
        name (str): name of state

    """

    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', backref='state', cascade='all, delete')
    else:
        @property
        def cities(self):
            """Cities"""
            all_cities = models.engine.all(City)
            all_cities_state = []
            for key, value in all_cities.items():
                if self.id == value.state_id:
                    all_cities_state.append(value)
            return all_cities_state
