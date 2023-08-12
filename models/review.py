#!/usr/bin/python3
"""A review class module

Class Description:
The Review class represents user reviews associated with places
or accommodations. It includes attributes such as place_id, user_id,
and text. The place_id links a review to a specific place
(using the Place.id attribute), while user_id connects the review to
the user who wrote it (using the User.id attribute). The text attribute
stores the content of the review. Instances of this class enable the
management of user feedback and opinions.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """A user review class that inherits from BaseModel and
    It includes attributes such as place_id, user_id, and text.
    """
    place_id = ""
    user_id = ""
    text = ""
