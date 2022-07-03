#!/usr/bin/python3

"""
serializes instances to a JSON file
and deserializes JSON file to instances
"""

import json
import os
from models.base_model import BaseModel


class FileStorage:
    """New class"""

    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        pass

    def all(self):
        """returns dict"""
        return self.__objects

    def new(self, obj):
        """sets in __objects dict a new obj"""
        a = obj.__class__.__name__
        self.__objects[a + "." + obj.id] = obj

    def save(self):
        """serializes"""
        copy = {}
        for key, value in self.__objects.items():
            copy.update([(key, value.to_dict())])
        with open(self.__file_path, "w+") as fil:
            json.dump(copy, fil)

    def reload(self):
        """ deserializes the JSON file to """
        if os.path.exists(FileStorage.__file_path) is True:
            with open(FileStorage.__file_path, "r") as f:
                obj = json.load(f)
            self.__objects = {}
            for key, value in obj.items():
                classs = value["__class__"]
                self.__objects[key] = eval(classs)(value)

    @staticmethod
    def class_list():
        """list of all classes"""
        return ["BaseModel", "User", "State",
                "City", "Amenity", "Place", "Review"]

    def delete(self, key):
        """deletes an instance"""
        FileStorage.__objects.pop(key)
