#!/usr/bin/python3
"""Module: place
This module defines the Place Class to AirBnB project.

Atributes:
    city_id (str): it will be the City.id
    user_id (str): it will be the User.id
    name (str): name of the place
    description (str): description of place
    number_rooms (int): number of rooms in a place
    number_bathrooms (int): number of bathrooms in a place
    max_guest (int): max of guest in a place
    price_by_night (int): price by nighe in a place
    latitude (float): latitude location
    longitude (float): longitud location
    amenity_ids (list): list of string it will be the list of Amenity.id later

"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """Class Place
    Inherits BaseModel
    Creates class attributes for Place class.

    Atributes:
        city_id (str): it will be the City.id
        user_id (str): it will be the User.id
        name (str): name of the place
        description (str): description of place
        number_rooms (int): number of rooms in a place
        number_bathrooms (int): number of bathrooms in a place
        max_guest (int): max of guest in a place
        price_by_night (int): price by nighe in a place
        latitude (float): latitude location
        longitude (float): longitud location
        amenity_ids (list): list of string it will be the list
                            of Amenity.id later

    """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = relationship("Review", backref="place", cascade="all,delete")
