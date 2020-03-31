#!/usr/bin/python3
"""Module: base_model
This module defines the BaseModel Class to AirBnB project.

Atributes:
    id (str): assign with an uuid when an instance is created
    created_at (datetime): assign with the current datetime
                           when an instance is created
    updated_at (datetime): assign with the current datetime when
                           an instance is created and it will be
                           updated every time you change your objec
t
Modifications:
30-Mzo-2020
__init__:include id(uuid) whith kwargs
         add a new instan in __objects through models.storage.new(obj)
save: include created_at attrib

"""
import uuid
import models
from datetime import datetime
"""KC-> adding"""
from sqlalchemy import Column, Integer, String, DateTime
"""KC-> adding"""
from sqlalchemy.ext.declarative import declarative_base
"""KC-> adding"""
Base = declarative_base()

class BaseModel:
    """Class BaseModel
    BaseModel is the principal class to operate program
    Here the id and date are generated.

    Args:
        *args: list of data to create or modify an instance
        **kwargs: dictionary of data to create or modify an instanc
e

    Atributes:
        id (str): assign with an uuid when an instance is created
        created_at (datetime): assign with the current datetime
                               when an instance is created
        updated_at (datetime): assign with the current datetime whe
n
                               an instance is created and it will b
e
                               updated every time you change your o
bject
    """

    """KC add this block to create new attrs for this class"""
    id = Column(String(60), unique=True, nullable=False, primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow,
                        nullable=False)
    update_at = Column(DateTime, default=datetime.utcnow,
                       nullable=False)

    def __init__(self, *args, **kwargs):
        """Instantiation of base model class
        Args:
            args: it won't be used
            kwargs: arguments for the constructor of the BaseModel
        Attributes:
            id: unique id generated
            created_at: creation date
            updated_at: updated date
        """
        if kwargs:
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
        """returns a string
        Return:
            returns a string of class name, id, and dictionary
        """
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def __repr__(self):
        """return a string representaion
        """
        return self.__str__()

    def save(self):
        """updates the public instance attribute updated_at to current
        """
        self.updated_at = datetime.now()
        self.created_at = datetime.now()
        """KC add-> remove this line from  __init__"""
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """creates dictionary of the class  and returns
        Return:
            returns a dictionary of all the key values in __dict__
        """
        my_dict = dict(self.__dict__)
        my_dict["__class__"] = str(type(self).__name__)
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        return my_dict
