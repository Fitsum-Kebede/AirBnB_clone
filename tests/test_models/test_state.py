#!/usr/bin/python3
"""Defines unittests for models/state.py."""

import unittest
import os
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
        """Set up a State instance for testing."""
        self.state = State()

    def test__type_inst(self):
        """Test if the instance is of the correct type."""
        self.assertIsInstance(self.state, State)

    def test_id_is_str(self):
        """Test if id attribute is of string type."""
        self.assertIsInstance(self.state.id, str)

    def test_dateti_created_at(self):
        """Test if created_at attribute is of datetime type."""
        self.assertIsInstance(self.state.created_at, datetime)

    def test_dateti_updated_at(self):
        """Test if updated_at attribute is of datetime type."""
        self.assertIsInstance(self.state.updated_at, datetime)

    def test_attr_name(self):
        """Test if name attribute is of correct type."""
        self.assertEqual(str, type(State.name))

    def test_inst_single_ids(self):
        """Test if two State instances have unique ids."""
        diff_state = State()
        self.assertNotEqual(self.state.id, diff_state.id)

    def test_created_at_ord(self):
        """Test if created_at timestamps are in ascending order."""
        sleep(0.05)
        diff_state = State()
        self.assertLess(self.state.created_at, diff_state.created_at)

    def test_ord_updated_at(self):
        """Test if updated_at timestamps are in ascending order."""
        sleep(0.05)
        diff_state = State()
        self.assertLess(self.state.updated_at, diff_state.updated_at)

    def test_kwargs_inst(self):
        """Test instantiation with keyword arguments."""
        dattod = datetime.today()
        dattod_iso = dattod.isoformat()
        state = State(id="450", created_at=dattod_iso, updated_at=dattod_iso)
        self.assertEqual(state.id, "450")
        self.assertEqual(state.created_at, dattod)
        self.assertEqual(state.updated_at, dattod)

    def test_None_kwargs_inst_(self):
        """Test instantiation with None keyword arguments."""
        with self.assertRaises(TypeError):
            State(id=None, created_at=None, updated_at=None)

    def test_str_rep(self):
        """Test if __str__ method returns the correct string representation."""
        dattod = datetime.today()
        self.state.id = "102"
        self.state.created_at = self.state.updated_at = dattod
        expected_str = (
            f"[State] (102) {{'id': '102', "
            f"'created_at': {repr(dattod)}, 'updated_at': {repr(dattod)}}}"
        )
        self.assertEqual(str(self.state), expected_str)

    def test_save_single(self):
        """Test if the save method updates the updated_at attribute."""
        first_updated_at = self.state.updated_at
        self.state.save()
        self.assertLess(first_updated_at, self.state.updated_at)

    def test_updated_at_multi(self):
        """Test if consecutive saves update the updated_at attribute."""
        first_updated_at = self.state.updated_at
        self.state.save()
        second_updated_at = self.state.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        self.state.save()
        self.assertLess(second_updated_at, self.state.updated_at)

    def test_arg_save(self):
        """Test if save method raises TypeError with argument."""
        with self.assertRaises(TypeError):
            self.state.save(None)

    def test_to_dict_type(self):
        """Test if to_dict method returns a dictionary."""
        self.assertIsInstance(self.state.to_dict(), dict)

    def test_contains_keys_dict(self):
        """Test if to_dict method contains the correct keys."""
        st_dict = self.state.to_dict()
        self.assertIn("id", st_dict)
        self.assertIn("created_at", st_dict)
        self.assertIn("updated_at", st_dict)
        self.assertIn("__class__", st_dict)

    def test_dict_strs_dateti_attr(self):
        """Test if datetime attributes in to_dict method are strings."""
        st_dict = self.state.to_dict()
        self.assertIsInstance(st_dict["id"], str)
        self.assertIsInstance(st_dict["created_at"], str)
        self.assertIsInstance(st_dict["updated_at"], str)

    def test_output_dict(self):
        """Test the output of to_dict method."""
        datim = datetime.today()
        self.state.id = "786159"
        self.state.created_at = self.state.updated_at = datim
        expected_dict = {
            'id': '786159',
            '__class__': 'State',
            'created_at': datim .isoformat(),
            'updated_at': datim .isoformat(),
        }
        self.assertDictEqual(self.state.to_dict(), expected_dict)

    def test_cont_dunder(self):
        """Test if to_dict output differs from __dict__."""
        self.assertNotEqual(self.state.to_dict(), self.state.__dict__)

    def test_arg_dict(self):
        """Test if to_dict method raises TypeError with invalid argument."""
        with self.assertRaises(TypeError):
            self.state.to_dict(None)


if __name__ == "__main__":
    unittest.main()
