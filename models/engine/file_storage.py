#!/usr/bin/python3
"""This module define the FileStorage that serializes instances
to a JSON file and deserializes JSON file to instances

Module Description:
The FileStorage module implements a storage mechanism for serializing
instances into a JSON file and deserializing instances from the JSON
file back into memory. This module acts as a bridge between the
object-oriented realm and the persistent storage layer. It offers
methods to store and retrieve instances, maintaining them across program
launches. By converting instances to JSON strings and storing them in a file,
the FileStorage module enables persistence and seamless data recovery.
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
    """FileStorage class definition and provides instance
    storage operations.

    Private class attributes:
        __file_path: string - path to the JSON file.
        __objects: dictionary - empty but will store all
                            objects by <class name>.id
    Public instance methods:
        all(self): returns the dictionary __objects
        new(self, obj): sets in __objects the obj with key <obj class name>.id
        save(self): serializes __objects to the JSON file (path: __file_path)
        reload(self): deserializes the JSON file to __objects
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects to saved is json file"""
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
                if data:
                    for key, value in data.items():
                        name = key.split(".")
                        self.__objects[key] = classes_dict[name[0]](**value)
                else:
                    self.__objects = {}
        except FileNotFoundError:
            pass
