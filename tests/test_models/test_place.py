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
        place = Place(id="415", created_at=current_time_iso,
                      updated_at=current_time_iso)
        self.assertEqual(place.id, "415")
        self.assertEqual(place.created_at, current_time)
        self.assertEqual(place.updated_at, current_time)

    def test_inst_None_kwar(self):
        """Test instantiation with None keyword arguments."""
        with self.assertRaises(TypeError):
            Place(id=None, created_at=None, updated_at=None)

    def test_type_inst(self):
        """Test if the instance is of the correct type."""
        self.assertIsInstance(self.test_place, Place)

    def test_attr_city_id(self):
        """Test if city_id attribute is of correct type."""
        self.assertEqual(str, type(Place.city_id))

    def test_attr_user_id(self):
        """Test if user_id attribute is of correct type."""
        self.assertEqual(str, type(Place.user_id))

    def test_str_id(self):
        """Test if id attribute is of string type."""
        self.assertEqual(str, type(self.test_place.id))

    def test_created_at_dateti(self):
        """Test if created_at attribute is of datetime type."""
        self.assertEqual(datetime, type(self.test_place.created_at))

    def test_attr_max_guest(self):
        """Test if max_guest attribute is of correct type."""
        self.assertEqual(int, type(Place.max_guest))

    def test_updated_at_dateti(self):
        """Test if updated_at attribute is of datetime type."""
        self.assertEqual(datetime, type(self.test_place.updated_at))

    def test_attr_descr(self):
        """Test if description attribute is of correct type."""
        self.assertEqual(str, type(Place.description))

    def test_attr_no_rooms(self):
        """Test if number_rooms attribute is of correct type."""
        self.assertEqual(int, type(Place.number_rooms))

    def test_attr_no_bathrooms(self):
        """Test if number_bathrooms attribute is of correct type."""
        self.assertEqual(int, type(Place.number_bathrooms))

    def test_attr_latitude(self):
        """Test if latitude attribute is of correct type."""
        self.assertEqual(float, type(Place.latitude))

    def test_attr_longitude(self):
        """Test if longitude attribute is of correct type."""
        self.assertEqual(float, type(Place.longitude))

    def test_attr_name(self):
        """Test if name attribute is of correct type."""
        self.assertEqual(str, type(Place.name))

    def test_attr_amenity_ids(self):
        """Test if amenity_ids attribute is of correct type."""
        self.assertEqual(list, type(Place.amenity_ids))

    def test__unique_two_places(self):
        """Test if two Place instances have unique ids."""
        place1 = Place()
        place2 = Place()
        self.assertNotEqual(place1.id, place2.id)

    def test_unused_args(self):
        """Test if unused arguments are not added to the instance."""
        place = Place(None)
        self.assertNotIn(None, place.__dict__.values())

    def test_rep_str(self):
        """Test if __str__ method returns the correct string representation."""
        current_time = datetime.today()
        current_time_repr = repr(current_time)
        self.test_place.id = "459725"
        self.test_place.created_at = self.test_place.updated_at = current_time
        place_str = str(self.test_place)
        self.assertIn("[Place] (459725)", place_str)
        self.assertIn("'id': '459725'", place_str)
        self.assertIn("'created_at': " + current_time_repr, place_str)
        self.assertIn("'updated_at': " + current_time_repr, place_str)

    def test_difrnt_created_two_places(self):
        """Test if two Place instances have different created_at timestamps."""
        place1 = Place()
        sleep(0.05)
        place2 = Place()
        self.assertLess(place1.created_at, place2.created_at)

    def test_difrnt_updated_at_two_places(self):
        """Test if two Place instances have different updated_at timestamps."""
        place1 = Place()
        sleep(0.05)
        place2 = Place()
        self.assertLess(place1.updated_at, place2.updated_at)

    def test_night_attribute_price(self):
        """Test if price_by_night attribute is of correct type."""
        self.assertEqual(int, type(Place.price_by_night))

    def test_save_one(self):
        """Test if the save method updates the updated_at attribute."""
        sleep(0.05)
        t_first_updated_at = self.test_place.updated_at
        self.test_place.save()
        self.assertLess(t_first_updated_at, self.test_place.updated_at)

    def test_saves_two(self):
        """Test if consecutive saves update the updated_at attribute."""
        sleep(0.05)
        to_first_updated_at = self.test_place.updated_at
        self.test_place.save()
        tso_second_updated_at = self.test_place.updated_at
        sleep(0.05)
        self.test_place.save()
        self.assertLess(tso_second_updated_at, self.test_place.updated_at)

    def test_arg_save(self):
        """Test if save method raises TypeError with argument."""
        with self.assertRaises(TypeError):
            self.test_place.save(None)

    def test_contains_correct_keys_to_dict(self):
        """Test if to_dict method contains the correct keys."""
        place_dict = self.test_place.to_dict()
        self.assertIn("id", place_dict)
        self.assertIn("created_at", place_dict)
        self.assertIn("updated_at", place_dict)
        self.assertIn("__class__", place_dict)

    def test_contains_added_attr_to_dict(self):
        """Test if to_dict method contains added attributes."""
        self.test_place.middle_name = "abc"
        self.test_place.my_number = 50
        self.assertEqual("abc", self.test_place.middle_name)
        self.assertIn("my_number", self.test_place.to_dict())

    def test_invalid_argument_to_dict(self):
        """Test if to_dict method raises TypeError with invalid argument."""
        with self.assertRaises(TypeError):
            self.test_place.to_dict(None)

    def test_dateti_attr_are_strs__to_dict_(self):
        """Test if datetime attributes in to_dict method are strings."""
        place_dict = self.test_place.to_dict()
        self.assertEqual(str, type(place_dict["id"]))
        self.assertEqual(str, type(place_dict["created_at"]))
        self.assertEqual(str, type(place_dict["updated_at"]))

    def test_output_to_dict(self):
        """Test the output of to_dict method."""
        current_time = datetime.today()
        self.test_place.id = "458745"
        self.test_place.created_at = self.test_place.updated_at = current_time
        expected_dict = {
            'id': '458745',
            '__class__': 'Place',
            'created_at': current_time.isoformat(),
            'updated_at': current_time.isoformat(),
        }
        self.assertDictEqual(self.test_place.to_dict(), expected_dict)


if __name__ == "__main__":
    unittest.main()
