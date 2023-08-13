#!/usr/bin/python3
"""Defines unittests for models/state.py."""

import os
import unittest
from datetime import datetime
from time import sleep
from models.state import State


class TestStateMethods(unittest.TestCase):
    """Unittests for the State class."""

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
        self.state = State()

    def test_instance_type(self):
        self.assertIsInstance(self.state, State)

    def test_id_is_str(self):
        self.assertIsInstance(self.state.id, str)

    def test_created_at_is_datetime(self):
        self.assertIsInstance(self.state.created_at, datetime)

    def test_updated_at_is_datetime(self):
        self.assertIsInstance(self.state.updated_at, datetime)

    def test_name_attribute(self):
        self.assertEqual(str, type(State.name))

    def test_unique_ids(self):
        another_state = State()
        self.assertNotEqual(self.state.id, another_state.id)

    def test_created_at_order(self):
        sleep(0.05)
        another_state = State()
        self.assertLess(self.state.created_at, another_state.created_at)

    def test_updated_at_order(self):
        sleep(0.05)
        another_state = State()
        self.assertLess(self.state.updated_at, another_state.updated_at)

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        state = State(id="450", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(state.id, "450")
        self.assertEqual(state.created_at, dt)
        self.assertEqual(state.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            State(id=None, created_at=None, updated_at=None)

    def test_str_representation(self):
        dt = datetime.today()
        self.state.id = "102"
        self.state.created_at = self.state.updated_at = dt
        expected_str = (
            f"[State] (102) {{'id': '102', "
            f"'created_at': {repr(dt)}, 'updated_at': {repr(dt)}}}"
        )
        self.assertEqual(str(self.state), expected_str)

    def test_one_save(self):
        first_updated_at = self.state.updated_at
        self.state.save()
        self.assertLess(first_updated_at, self.state.updated_at)

    def test_multiple_saves_updated_at(self):
        first_updated_at = self.state.updated_at
        self.state.save()
        second_updated_at = self.state.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        self.state.save()
        self.assertLess(second_updated_at, self.state.updated_at)

    def test_save_with_argument(self):
        with self.assertRaises(TypeError):
            self.state.save(None)

    def test_to_dict_type(self):
        self.assertIsInstance(self.state.to_dict(), dict)

    def test_to_dict_contains_keys(self):
        st_dict = self.state.to_dict()
        self.assertIn("id", st_dict)
        self.assertIn("created_at", st_dict)
        self.assertIn("updated_at", st_dict)
        self.assertIn("__class__", st_dict)

    def test_to_dict_contains_added_attributes(self):
        self.state.middle_name = "Holberton"
        self.state.my_number = 98
        self.assertEqual("Holberton", self.state.middle_name)
        self.assertIn("my_number", self.state.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        st_dict = self.state.to_dict()
        self.assertIsInstance(st_dict["id"], str)
        self.assertIsInstance(st_dict["created_at"], str)
        self.assertIsInstance(st_dict["updated_at"], str)

    def test_to_dict_output(self):
        dt = datetime.today()
        self.state.id = "786159"
        self.state.created_at = self.state.updated_at = dt
        expected_dict = {
            'id': '786159',
            '__class__': 'State',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(self.state.to_dict(), expected_dict)

    def test_contrast_to_dict_dunder_dict(self):
        self.assertNotEqual(self.state.to_dict(), self.state.__dict__)

    def test_to_dict_with_argument(self):
        with self.assertRaises(TypeError):
            self.state.to_dict(None)


if __name__ == "__main__":
    unittest.main()
