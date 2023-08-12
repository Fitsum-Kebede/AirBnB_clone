#!/usr/bin/python3
"""A place class module

Class Description:
The Place class models accommodations or places that can be
rented or reserved. It encompasses several attributes including city_id,
user_id, name, description, number_rooms, number_bathrooms, max_guest,
price_by_night, latitude, longitude, and amenity_ids. These attributes
store details related to the place's location, features, and amenities.
Instances of this class facilitate property management and reservations.
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """A class that represent a rental place and It encompasses
    several attributes including city_id, user_id, name, description,
    number_rooms, number_bathrooms, max_guest,
    price_by_night, latitude, longitude, and amenity_ids
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
