#!/usr/bin/python3
"""Module: user
This module defines the User Class to AirBnB project.

Atributes:
    email (str): email of user
    password (str): password of user
    first_name (str): first name of user
    last_name (str): lasr name of user

"""


from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.review import Review
from models.place import Place


class User(BaseModel, Base):
    """Class User
    Inherits User
    Creates class attributes for User Class

    Atributes:
        email (str): email of user
        password (str): password of user
        first_name (str): first name of user
        last_name (str): lasr name of user
    """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    places = relationship("Place", backref="user", cascade="all, delete")
    reviews = relationship("Review", backref="user", cascade="all, delete")
