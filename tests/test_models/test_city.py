#!/usr/bin/python3
"""Defines unittests for models/city.py."""

import unittest
import os
import models
from datetime import datetime
from time import sleep
from models.city import City


class TestCityMethods(unittest.TestCase):
    """Unittests for the City class."""

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
        """Set up a City instance for testing."""
        self.city = City()

    # Test cases for City class instantiation

    def test__inst_no_args(self):
        """Test if City class can be instantiated without arguments."""
        self.assertEqual(City, type(self.city))

    def testpublic_str_id(self):
        """Test if id attribute is of string type."""
        self.assertEqual(str, type(self.city.id))

    def test_public_dateti_created_at(self):
        """Test if created_at attribute is of datetime type."""
        self.assertEqual(datetime, type(self.city.created_at))

    def test_public_dateti_updated_at(self):
        """Test if updated_at attribute is of datetime type."""
        self.assertEqual(datetime, type(self.city.updated_at))

    def test_public_class_attr_state_id(self):
        """Test if state_id attribute is a public class attribute."""
        self.assertEqual(str, type(City.state_id))
        self.assertIn("state_id", dir(self.city))
        self.assertNotIn("state_id", self.city.__dict__)

    def test_public_class_attr_name(self):
        """Test if name attribute is a public class attribute."""
        self.assertEqual(str, type(City.name))
        self.assertIn("name", dir(self.city))
        self.assertNotIn("name", self.city.__dict__)

    def test_double_cities_diff_ids(self):
        """Test if two City instances have unique ids."""
        diff_city = City()
        self.assertNotEqual(self.city.id, diff_city.id)

    def test_double_cities_diff_created_at(self):
        """Test if two City instances have different created_at timestamps."""
        diff_city = City()
        sleep(0.05)
        self.assertLess(self.city.created_at, diff_city.created_at)

    def test_double_cities_diff_updated_at(self):
        """Test if two City instances have different updated_at timestamps."""
        diff_city = City()
        sleep(0.05)
        self.assertLess(self.city.updated_at, diff_city.updated_at)

    def test_repr_str(self):
        """Test if __str__ method returns the correct string representation."""
        dayto = datetime.today()
        dayto_repr = repr(dayto)
        self.city.id = "759786"
        self.city.created_at = self.city.updated_at = dayto
        string_city = str(self.city)
        self.assertIn("[City] (759786)", string_city)
        self.assertIn("'id': '759786'", string_city)
        self.assertIn("'created_at': " + dayto_repr, string_city)
        self.assertIn("'updated_at': " + dayto_repr, string_city)

    def test_unused_argument(self):
        """Test if unused arguments are not added to the instance."""
        city = City(None)
        self.assertNotIn(None, city.__dict__.values())

    def test_inst_kwargs(self):
        """Test instantiation with keyword arguments."""
        dayto = datetime.today()
        dayto_iso = dayto.isoformat()
        city = City(id="235", created_at=dayto_iso, updated_at=dayto_iso)
        self.assertEqual(city.id, "235")
        self.assertEqual(city.created_at, dayto)
        self.assertEqual(city.updated_at, dayto)

    def test_inst_No_kwargs(self):
        """Test instantiation with None keyword arguments."""
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)

    def test_single_save(self):
        """Test if the save method updates the updated_at attribute."""
        sleep(0.05)
        first_updated_at = self.city.updated_at
        self.city.save()
        self.assertLess(first_updated_at, self.city.updated_at)

    def test_double_saves(self):
        """Test if consecutive saves update the updated_at attribute."""
        sleep(0.05)
        first_updated_at = self.city.updated_at
        self.city.save()
        second_updated_at = self.city.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        self.city.save()
        self.assertLess(second_updated_at, self.city.updated_at)

    def test_argument_save(self):
        """Test if save method raises TypeError with argument."""
        with self.assertRaises(TypeError):
            self.city.save(None)

    def test_type_dict(self):
        """Test if to_dict method returns a dictionary."""
        self.assertTrue(dict, type(self.city.to_dict()))

    def test_contains_right_keys_dict(self):
        """Test if to_dict method contains the correct keys."""
        city_dictionary = self.city.to_dict()
        self.assertIn("id", city_dictionary)
        self.assertIn("created_at", city_dictionary)
        self.assertIn("updated_at", city_dictionary)
        self.assertIn("__class__", city_dictionary)

    def test_have_added_attr_dict(self):
        """Test if to_dict method contains added attributes."""
        self.city.middle_name = "Addis"
        self.city.my_number = 10
        self.assertEqual("Addis", self.city.middle_name)
        self.assertIn("my_number", self.city.to_dict())

    def test_dateti_attr_strs_dict(self):
        """Test if datetime attributes in to_dict method are strings."""
        city_dict = self.city.to_dict()
        self.assertEqual(str, type(city_dict["id"]))
        self.assertEqual(str, type(city_dict["created_at"]))
        self.assertEqual(str, type(city_dict["updated_at"]))

    def test_dict_output(self):
        """Test the output of to_dict method."""
        dayto = datetime.today()
        self.city.id = "135976"
        self.city.created_at = self.city.updated_at = dayto
        expected_result = {
            'id': '135976',
            '__class__': 'City',
            'created_at': dayto.isoformat(),
            'updated_at': dayto.isoformat(),
        }
        self.assertDictEqual(self.city.to_dict(), expected_result)

    def test_dict_dunder_dict(self):
        """Test if to_dict output differs from __dict__."""
        self.assertNotEqual(self.city.to_dict(), self.city.__dict__)

    def test_arg_dict(self):
        """Test if to_dict method raises TypeError with invalid argument."""
        with self.assertRaises(TypeError):
            self.city.to_dict(None)


if __name__ == "__main__":
    unittest.main()
