#!/usr/bin/python3
"""Module: file_storage
This module defines the FileStorage Class to AirBnB project.
Used to access and edit a JSON file

Args:
    obj (obj): input instance of object used to create a new in dic
tionary

Atributes:
    __file_path (str): path to the JSON file (ex: file.json)
    __objects (dict): store all objects by <class name>.id

Update by:
Date:31-Mzo-2020
Author: Ivan Dario Lasso:
Task5 to take a classname(cls) in instance method all
if class arg is Not None return only specific class registers
add instance method delete to delete an id to de __objects dict

"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import sys


class FileStorage:
    """This class serializes instances to a JSON file and
    deserializes JSON file to instances
    Attributes:
        __file_path: path to the JSON file
        __objects: objects will be stored
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """returns a dictionary
        Return:
            returns a dictionary of __object
        """
        if cls is None:
            return self.__objects
        # if cls arg has a value return new dict only whith specific
        # class registers
        dictionary = {}
        for i, j in self.__objects.items():
            if j.__class__ == cls:
                dictionary[i] = j
        return dictionary

    def new(self, obj):
        """sets __object to given obj
        Args:
            obj: given object
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """serialize the file path to JSON file path
        """
        my_dict = {}
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(my_dict, f)

    def reload(self):
        """serialize the file path to JSON file path
        """
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """to delete obj from __objects if it’s inside
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            del self.__objects[key]
            self.save()
