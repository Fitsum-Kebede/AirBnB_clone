#!/usr/bin/python3
"""This module define the FileStorage that serializes instances
to a JSON file and deserializes JSON file to instances
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """FileStorage class definition"""
    __file_path = "airbnb.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id

        args:
            obj: A dictionary to be set as a value to <obj class name>.id
            as key/pair values of __objects dictionary.
        Returns: nothing
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)

        Returns: nothing
        """
        data = {}
        for key in self.__objects:
            data[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(data, file)

    def reload(self):
        """Deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)

        Returns: nothing
        """
        classes_dict = {"BaseModel": BaseModel, "User": User, "City": City,
                        "Review": Review, "Amenity": Amenity, "Place": Place,
                        "State": State}
        try:
            with open(self.__file_path, "r") as file:
                data = json.load(file)
                for key, value in data.items():
                    name = key.split(".")
                    self.__objects[key] = classes_dict[name[0]](**value)
        except FileNotFoundError:
            pass
