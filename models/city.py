#!/usr/bin/python3
"""A city class module.

Class Description:
The City class models a city within a state and is integral to the
application's data structure. It has two main attributes: state_id
and name. The state_id associates a city with a particular state (using
the State.id attribute). The name attribute stores the name of the city.
Instances of this class allow for location-specific information management.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """A class city that inherits from BaseModel and has
    attributes state_id and name for access and specifically stores
    city name.
    """
    state_id = ""
    name = ""
