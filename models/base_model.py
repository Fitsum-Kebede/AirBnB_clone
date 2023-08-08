#!/usr/bin/python3
"""This module define BaseModel class which defines all
common attrbute and methods for subclasses.
"""
import datetime
from uuid import uuid4


class BaseModel:
    """BaseModel class  definition"""
    def __init__(self):
        """Instatiate the BaseModel instance with unique id,
        the date the instance or object is created and the date
        at the which the instance or object was modified or updated.
        """
        self.id = str(uuid4())
        self.created_at = datetime.datetime.today()
        self.updated_at = datetime.datetime.today()

    def __str__(self):
        """Returns the string representation of the BaseModel"""
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """Sets the date at which the BaseModel object has been updated"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """Returns BaseModel dictionary"""
        model_dict = {}
        self.__dict__["__class__"] = self.__class__.__name__
        for key, value in self.__dict__.items():
            if key == "created_at":
                value = value.isoformat()
            if key == "updated_at":
                value = value.isoformat()
            model_dict[key] = value
        return (model_dict)
