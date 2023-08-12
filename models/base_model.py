#!/usr/bin/python3
"""This module define BaseModel class which defines all
common attrbute and methods for subclasses.
"""
from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    """BaseModel class  definition"""
    def __init__(self, *args, **kwargs):
        """Instatiate the BaseModel instance with unique id,
        the date the instance or object is created and the date
        at the which the instance or object was modified or updated.

        args:
            args: won’t be used
            kwargs: key/value pair of the BaseModel instance to be used
                    create another BaseModel object.
        """
        self.id = str(uuid4())
        self.created_at = self.updated_at = datetime.today()
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        value = datetime.strptime(value,
                                                  "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)

    def __str__(self):
        """Returns the string representation of the BaseModel"""
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """Sets the date at which the BaseModel object has been updated"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Returns BaseModel dictionary"""
        model_dict = {}
        model_dict["__class__"] = self.__class__.__name__
        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                value = value.isoformat()
            model_dict[key] = value
        return (model_dict)
