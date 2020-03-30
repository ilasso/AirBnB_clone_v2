#!/usr/bin/python3
"""Module: user
This module defines the User Class to AirBnB project.

Atributes:
    email (str): email of user
    password (str): password of user
    first_name (str): first name of user
    last_name (str): lasr name of user

"""


from models.base_model import BaseModel


class User(BaseModel):
    """Class User
    Inherits from User
    Creates class attributes for User Class
 
    Atributes:
        email (str): email of user
        password (str): password of user
        first_name (str): first name of user
        last_name (str): lasr name of user
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
