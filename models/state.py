#!/usr/bin/python3
"""
This module defines the State Class to AirBnB project.
"""


from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
import models
import os


class State(BaseModel, Base):
    """Creates class attributes for State Class"""

    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City',
                              backref='state',
                              cascade='all, delete-orphan')
    else:
        @property
        def cities(self):
            """Cities"""
            lista = []
            for i, j in models.storage.all().items():
                if j.__class__.__name__ == 'City':
                    if j.state_id == self.id:
                        lista.append(j)
            return lista
