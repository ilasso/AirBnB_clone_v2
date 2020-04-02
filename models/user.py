#!/usr/bin/python3
"""
This module defines the User Class to AirBnB project.
"""


from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.review import Review
from models.place import Place


class User(BaseModel, Base):
    """Creates class attributes for User Class"""
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    places = relationship("Place", backref="user", cascade="all, delete")
    reviews = relationship("Review", backref="user", cascade="all, delete")
