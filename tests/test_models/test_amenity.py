#!/usr/bin/python3
"""Defines unittests for models/amenity.py."""

import unittest
import os
from datetime import datetime
from time import sleep
from models.amenity import Amenity


class TestAmenityMethods(unittest.TestCase):
    """Test cases for the Amenity class."""

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
        self.amenity = Amenity()

    def test_type_ins(self):
        self.assertIsInstance(self.amenity, Amenity)

    def test_id_str(self):
        self.assertIsInstance(self.amenity.id, str)

    def test__dateti_created_at(self):
        self.assertIsInstance(self.amenity.created_at, datetime)

    def test_dateti_updated_at(self):
        self.assertIsInstance(self.amenity.updated_at, datetime)

    def test_attr_name(self):
        self.assertEqual(str, type(Amenity.name))

    def test_ids_is_unique(self):
        another_amenity = Amenity()
        self.assertNotEqual(self.amenity.id, another_amenity.id)

    def test_ord_created_at(self):
        sleep(0.05)
        another_amenity = Amenity()
        self.assertLess(self.amenity.created_at, another_amenity.created_at)

    def test_ord_updated_at(self):
        sleep(0.05)
        another_amenity = Amenity()
        self.assertLess(self.amenity.updated_at, another_amenity.updated_at)

    def test_repre_of_str(self):
        tym = datetime.today()
        tym_repr = repr(tym)
        self.amenity.id = "527"
        self.amenity.created_at = self.amenity.updated_at = tym
        expected_str = (
            f"[Amenity] (527) {{'id': '527', "
            f"'created_at': {repr(tym)}, 'updated_at': {repr(tym)}}}"
        )
        self.assertEqual(str(self.amenity), expected_str)

    def test_inst_kwargs(self):
        tym = datetime.today()
        tym_iso = tym.isoformat()
        amenity = Amenity(id="400", created_at=tym_iso, updated_at=tym_iso)
        self.assertEqual(amenity.id, "400")
        self.assertEqual(amenity.created_at, tym)
        self.assertEqual(amenity.updated_at, tym)

    def test_inst_None_kwargs(self):
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)

    def test_save(self):
        sleep(0.05)
        first_updated_at = self.amenity.updated_at
        self.amenity.save()
        self.assertLess(first_updated_at, self.amenity.updated_at)

    def test__saves_updated_multiple(self):
        sleep(0.05)
        first_updated_at = self.amenity.updated_at
        self.amenity.save()
        second_updated_at = self.amenity.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        self.amenity.save()
        self.assertLess(second_updated_at, self.amenity.updated_at)

    def test_argument_saves(self):
        with self.assertRaises(TypeError):
            self.amenity.save(None)

    def test_save_file_upda(self):
        self.amenity.save()
        amid = "Amenity." + self.amenity.id
        with open("file.json", "r") as file:
            self.assertIn(amid, file.read())

    def test_type_dict(self):
        self.assertIsInstance(self.amenity.to_dict(), dict)

    def test_cont_keys_dict(self):
        amenity_dict = self.amenity.to_dict()
        self.assertIn("id", amenity_dict)
        self.assertIn("created_at", amenity_dict)
        self.assertIn("updated_at", amenity_dict)
        self.assertIn("__class__", amenity_dict)

    def test__dict_added_attri_contains(self):
        self.amenity.middle_name = "abc"
        self.amenity.my_number = 70
        self.assertEqual("abc", self.amenity.middle_name)
        self.assertIn("my_number", self.amenity.to_dict())

    def test_attributes_strs_dict_dateti(self):
        am_dict = self.amenity.to_dict()
        self.assertIsInstance(am_dict["id"], str)
        self.assertIsInstance(am_dict["created_at"], str)
        self.assertIsInstance(am_dict["updated_at"], str)

    def test__output_dict(self):
        tym = datetime.today()
        self.amenity.id = "875652"
        self.amenity.created_at = self.amenity.updated_at = tym
        expected_dict = {
            'id': '875652',
            '__class__': 'Amenity',
            'created_at': tym.isoformat(),
            'updated_at': tym.isoformat(),
        }
        self.assertDictEqual(self.amenity.to_dict(), expected_dict)

    def test_under_dict_contrast(self):
        self.assertNotEqual(self.amenity.to_dict(), self.amenity.__dict__)

    def test__argument_dict(self):
        with self.assertRaises(TypeError):
            self.amenity.to_dict(None)


if __name__ == "__main__":
    unittest.main()
