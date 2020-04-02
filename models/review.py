#!/usr/bin/python3
"""
This module defines the Review Class to AirBnB project.
"""


from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class Review(BaseModel, Base):
    """Creates class attributes for Review Class"""

    __tablename__ = "reviews"
    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    text = Column(String(1024), nullable=False)
