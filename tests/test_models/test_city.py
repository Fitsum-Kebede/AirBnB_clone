#!/usr/bin/python3
"""Defines unittests for models/place.py."""

import unittest
import os
from datetime import datetime
from time import sleep
from models.place import Place


class TestPlaceMethods(unittest.TestCase):
    """Test cases for the Place class."""

    @classmethod
    def setUpClass(cls):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDownClass(cls):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def setUp(self):
        self.test_place = Place()

    def test_inst_kwar(self):
        """Test instantiation with keyword arguments."""
        current_time = datetime.today()
        current_time_iso = current_time.isoformat()
        place = Place(id="325", created_at=current_time_iso, updated_at=current_time_iso)
        self.assertEqual(place.id, "325")
        self.assertEqual(place.created_at, current_time)
        self.assertEqual(place.updated_at, current_time)

    def test_inst_None_kwar(self):
        """Test instantiation with None keyword arguments."""
        with self.assertRaises(TypeError):
            Place(id=None, created_at=None, updated_at=None)

    def test_type_inst(self):
        """Test if the instance is of the correct type."""
        self.assertIsInstance(self.test_place, Place)

    def test__id_attr_city(self):
        """Test if city_id attribute is of correct type."""
        self.assertEqual(str, type(Place.city_id))

    def test_id_attr_user(self):
        """Test if user_id attribute is of correct type."""
        self.assertEqual(str, type(Place.user_id))

    def test_str_id(self):
        """Test if id attribute is of string type."""
        self.assertEqual(str, type(self.test_place.id))

    def test__dateti_created_at(self):
        """Test if created_at attribute is of datetime type."""
        self.assertEqual(datetime, type(self.test_place.created_at))

    def test_dateti_updated_at(self):
        """Test if updated_at attribute is of datetime type."""
        self.assertEqual(datetime, type(self.test_place.updated_at))

    def test_attribute_dateti(self):
        """Test if description attribute is of correct type."""
        self.assertEqual(str, type(Place.description))

    def test_attr_no_rooms(self):
        """Test if number_rooms attribute is of correct type."""
        self.assertEqual(int, type(Place.number_rooms))

    def test_attr_no_bathrooms(self):
        """Test if number_bathrooms attribute is of correct type."""
        self.assertEqual(int, type(Place.number_bathrooms))

    def test_attr_max_guest(self):
        """Test if max_guest attribute is of correct type."""
        self.assertEqual(int, type(Place.max_guest))

    def test_max_guest_latitude_attr(self):
        """Test if latitude attribute is of correct type."""
        self.assertEqual(float, type(Place.latitude))

    def test_longitude_attribute(self):
        """Test if longitude attribute is of correct type."""
        self.assertEqual(float, type(Place.longitude))

    def test_attr_name(self):
        """Test if name attribute is of correct type."""
        self.assertEqual(str, type(Place.name))

    def test__ids_attr_amenity(self):
        """Test if amenity_ids attribute is of correct type."""
        self.assertEqual(list, type(Place.amenity_ids))

    def test_unique_two_places(self):
        """Test if two Place instances have unique ids."""
        placea = Place()
        placeb = Place()
        self.assertNotEqual(placea.id, placeb.id)

    def test_repr_str(self):
        """Test if __str__ method returns the correct string representation."""
        current_time = datetime.today()
        current_time_repr = repr(current_time)
        self.test_place.id = "159753"
        self.test_place.created_at = self.test_place.updated_at = current_time
        place_str = str(self.test_place)
        self.assertIn("[Place] (159753)", place_str)
        self.assertIn("'id': '159753'", place_str)
        self.assertIn("'created_at': " + current_time_repr, place_str)
        self.assertIn("'updated_at': " + current_time_repr, place_str)

    def test_dif_two_places_created_at(self):
        """Test if two Place instances have different created_at timestamps."""
        placea = Place()
        sleep(0.05)
        placeb = Place()
        self.assertLess(placea.created_at, placeb.created_at)

    def test_dif_two_places_updated_at(self):
        """Test if two Place instances have different updated_at timestamps."""
        placea = Place()
        sleep(0.05)
        placeb = Place()
        self.assertLess(placea.updated_at, placeb.updated_at)

    def test_night_attr_price(self):
        """Test if price_by_night attribute is of correct type."""
        self.assertEqual(int, type(Place.price_by_night))

    def test_save_one(self):
        """Test if the save method updates the updated_at attribute."""
        sleep(0.05)
        first_updated_at = self.test_place.updated_at
        self.test_place.save()
        self.assertLess(first_updated_at, self.test_place.updated_at)

    def test_saves_two(self):
        """Test if consecutive saves update the updated_at attribute."""
        sleep(0.05)
        first_updated_at = self.test_place.updated_at
        self.test_place.save()
        second_updated_at = self.test_place.updated_at
        sleep(0.05)
        self.test_place.save()
        self.assertLess(second_updated_at, self.test_place.updated_at)

    def test_arg_save(self):
        """Test if save method raises TypeError with argument."""
        with self.assertRaises(TypeError):
            self.test_place.save(None)

    def test_dict_type(self):
        """Test if to_dict method returns a dictionary."""
        self.assertTrue(dict, type(self.test_place.to_dict()))

    def test_contains_correct_keys_dict(self):
        """Test if to_dict method contains the correct keys."""
        place_dict = self.test_place.to_dict()
        self.assertIn("id", place_dict)
        self.assertIn("created_at", place_dict)
        self.assertIn("updated_at", place_dict)
        self.assertIn("__class__", place_dict)

    def test_attr_dict_contains_added(self):
        """Test if to_dict method contains added attributes."""
        self.test_place.middle_name = "abc"
        self.test_place.my_number = 10
        self.assertEqual("abc", self.test_place.middle_name)
        self.assertIn("my_number", self.test_place.to_dict())

    def test_strs_dict_dateti_attr(self):
        """Test if datetime attributes in to_dict method are strings."""
        place_dict = self.test_place.to_dict()
        self.assertEqual(str, type(place_dict["id"]))
        self.assertEqual(str, type(place_dict["created_at"]))
        self.assertEqual(str, type(place_dict["updated_at"]))

    def test_output_dict_(self):
        """Test the output of to_dict method."""
        current_time = datetime.today()
        self.test_place.id = "257954"
        self.test_place.created_at = self.test_place.updated_at = current_time
        expected_dict = {
            'id': '257954',
            '__class__': 'Place',
            'created_at': current_time.isoformat(),
            'updated_at': current_time.isoformat(),
        }
        self.assertDictEqual(self.test_place.to_dict(), expected_dict)


if __name__ == "__main__":
    unittest.main()

