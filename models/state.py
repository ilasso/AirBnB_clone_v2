#!/usr/bin/python3
"""
This module defines the State Class to AirBnB project.
"""


from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
import models
from os import getenv


class State(BaseModel, Base):
    """Creates class attributes for State Class"""

    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', backref='state', cascade='all, delete')
    else:
        @property
        def cities(self):
            """Cities"""
            all_cities = models.storage.all(City)
            all_cities_state = []
            for key, value in all_cities.items():
                if self.id == value.state_id:
                    all_cities_state.append(value)
            return all_cities_state
