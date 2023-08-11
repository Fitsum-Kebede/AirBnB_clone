#!/usr/bin/python3
"""A user class module"""
from models.base_model import BaseModel


class User(BaseModel):
    """A user class with attributes that inherits
    from the BaseModel with
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
