#!/usr/bin/python3
"""A user class module

Module Description:
The User class extends the functionality of the BaseModel class,
encapsulating user-related information within the application.
It represents individuals who interact with the system and provides
attributes for managing their profile details.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """A user class with attributes that inherits from the BaseModel.

    email: A string attribute that stores the email address
        associated with the user. It is initialized as an empty string
        and serves as a unique identifier for each user.
    password: A string attribute that stores the user's password.
        Like email, it is initialized as an empty string and ensures
        secure access to the user's account.
    first_name: A string attribute representing the user's first name.
        It starts as an empty string and is used to
        store the user's given name.
    last_name: A string attribute representing the user's last name.
        Similar to first_name, it initializes as an empty string
        and holds the user's surname.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
