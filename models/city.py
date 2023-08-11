#!/usr/bin/python3
"""A city class module"""
from models.base_model import BaseModel


class City(BaseModel):
    """A class city that inherits from BaseModel"""

    state_id = ""
    name = ""
