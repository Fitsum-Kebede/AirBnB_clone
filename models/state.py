#!/usr/bin/python3
"""A state class module

Class Description:
The State class represents a geographical state and is part of the data model.
It has a name attribute, which stores the name of the state. Instances of this
class serve as a means of organizing and categorizing locations within a larger
geographical context.
"""
from models.base_model import BaseModel


class State(BaseModel):
    """A state class with a name attributes to represent
    geographical state.
    """
    name = ""
