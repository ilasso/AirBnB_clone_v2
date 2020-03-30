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
    amenity_ids (list): list of string it will be the list of Ameni
ty.id later

"""

from models.base_model import BaseModel


class Place(BaseModel):
    """Class Place
    Inherits from BaseModel
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
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
