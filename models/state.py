#!/usr/bin/python3
"""Module: state
This module defines the State Class to AirBnB project.

Atributes:
    name (str): name of state

"""


from models.base_model import BaseModel


class State(BaseModel):
    """Class State
    Inherits from BaseModel
    Creates class attributes for State Class

    Atributes:
        name (str): name of state

    """

    name = ""
