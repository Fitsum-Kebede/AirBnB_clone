#!/usr/bin/python3
"""A review class module"""
from models.base_model import BaseModel


class Review(BaseModel):
    """A user review class that inherits from BaseModel"""

    place_id = ""
    user_id = ""
    text = ""
