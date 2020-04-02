#!/usr/bin/python3
"""
This module defines the BaseModel Class to AirBnB project.
"""


import uuid
import models
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseModel:
    """BaseModel is the principal class to operate program"""

    id = Column(String(60),
                unique=True,
                nullable=False,
                primary_key=True)

    created_at = Column(DateTime,
                        default=datetime.utcnow,
                        nullable=False)

    update_at = Column(DateTime,
                       default=datetime.utcnow,
                       nullable=False)

    def __init__(self, *args, **kwargs):
        """Instantiation of base model class updated_at: updated date"""
        if kwargs:
            if self.id is None:
                self.id = str(uuid.uuid4())
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """returns a string of class name, id, and dictionary"""
        if self.__dict__["_sa_instance_state"]:
            del self.__dict__["_sa_instance_state"]
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def __repr__(self):
        """return a string representaion"""
        return self.__str__()

    def save(self):
        """updates the public instance attribute updated_at to current"""
        self.updated_at = datetime.now()
        self.created_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """creates dictionary of the class  and returns values in __dict__"""
        my_dict = dict(self.__dict__)
        my_dict["__class__"] = str(type(self).__name__)
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        if '_sa_instance_state' in my_dict.keys():
            del my_dict['_sa_instance_state']

        return my_dict

    def delete(self):
        """delete instance method. delete a class"""
        models.storage.delete()
