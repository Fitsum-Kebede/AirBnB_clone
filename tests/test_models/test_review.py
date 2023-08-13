#!/usr/bin/python3
"""Defines unittests for models/review.py."""

import unittest
import os
from datetime import datetime
from time import sleep
from models.review import Review


class TestReviewMethods(unittest.TestCase):
    """Test cases for Review class."""
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
        self.review = Review()

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_insta_type(self):
        """Test if the instance is of the correct type."""
        self.assertIsInstance(self.review, Review)

    def test_str_id(self):
        """Test if id attribute is of string type."""
        self.assertIsInstance(self.review.id, str)

    def test__dateti_created_at(self):
        """Test if created_at attribute is of datetime type."""
        self.assertIsInstance(self.review.created_at, datetime)

    def test__dateti_updated_at(self):
        """Test if updated_at attribute is of datetime type."""
        self.assertIsInstance(self.review.updated_at, datetime)

    def test__attr_place(self):
        """Test if place_id attribute is of correct type."""
        self.assertEqual(str, type(Review.place_id))

    def test__attr_user(self):
        """Test if user_id attribute is of correct type."""
        self.assertEqual(str, type(Review.user_id))

    def test__attr_text(self):
        """Test if text attribute is of correct type."""
        self.assertEqual(str, type(Review.text))

    def test__ids_unique(self):
        """Test if two Review instances have unique ids."""
        another_review = Review()
        self.assertNotEqual(self.review.id, another_review.id)

    def test_ord_created_at(self):
        """Test if created_at timestamps are in ascending order."""
        sleep(0.05)
        another_review = Review()
        self.assertLess(self.review.created_at, another_review.created_at)

    def test__ordr_updated_at(self):
        """Test if updated_at timestamps are in ascending order."""
        sleep(0.05)
        another_review = Review()
        self.assertLess(self.review.updated_at, another_review.updated_at)

    def test_inst_kwargs(self):
        """Test instantiation with keyword arguments."""
        tym = datetime.today()
        tym_iso = tym.isoformat()
        review = Review(id="359", created_at=tym_iso, updated_at=tym_iso)
        self.assertEqual(review.id, "359")
        self.assertEqual(review.created_at, tym)
        self.assertEqual(review.updated_at, tym)

    def test_inst_None_kwargs(self):
        """Test instantiation with None keyword arguments."""
        with self.assertRaises(TypeError):
            Review(id=None, created_at=None, updated_at=None)

    def test_rep_str(self):
        """Test if __str__ method returns the correct string representation."""
        dt = datetime.today()
        self.review.id = "569439"
        self.review.created_at = self.review.updated_at = dt
        expected_str = (
            f"[Review] (569439) {{'id': '569439', "
            f"'created_at': {repr(dt)}, 'updated_at': {repr(dt)}}}"
        )
        self.assertEqual(str(self.review), expected_str)

    def test_save_updated_at_updates(self):
        """Test if the save method updates the updated_at attribute."""
        first_updated_at = self.review.updated_at
        self.review.save()
        self.assertLess(first_updated_at, self.review.updated_at)

    def test_saves_updated_at_multiple(self):
        """Test if consecutive saves update the updated_at attribute."""
        first_updated_at = self.review.updated_at
        self.review.save()
        second_updated_at = self.review.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        self.review.save()
        self.assertLess(second_updated_at, self.review.updated_at)

    def test_argument_save(self):
        """Test if save method raises TypeError with argument."""
        with self.assertRaises(TypeError):
            self.review.save(None)

    def test_dict_type(self):
        """Test if to_dict method returns a dictionary."""
        self.assertIsInstance(self.review.to_dict(), dict)

    def test_contains_keys_dict(self):
        """Test if to_dict method contains the correct keys."""
        rv_dict = self.review.to_dict()
        self.assertIn("id", rv_dict)
        self.assertIn("created_at", rv_dict)
        self.assertIn("updated_at", rv_dict)
        self.assertIn("__class__", rv_dict)

    def test_contains_added_attr_dict(self):
        """Test if to_dict method contains added attributes."""
        self.review.middle_name = "abc"
        self.review.my_number = 63
        self.assertEqual("abc", self.review.middle_name)
        self.assertIn("my_number", self.review.to_dict())

    def test_strs_dict_dateti_attr(self):
        """Test if datetime attributes in to_dict method are strings."""
        rv_dict = self.review.to_dict()
        self.assertIsInstance(rv_dict["id"], str)
        self.assertIsInstance(rv_dict["created_at"], str)
        self.assertIsInstance(rv_dict["updated_at"], str)

    def test_dict_output(self):
        """Test the output of to_dict method."""
        tym = datetime.today()
        self.review.id = "756843"
        self.review.created_at = self.review.updated_at = tym
        expected_dict = {
            'id': '756843',
            '__class__': 'Review',
            'created_at': tym.isoformat(),
            'updated_at': tym.isoformat(),
        }
        self.assertDictEqual(self.review.to_dict(), expected_dict)

    def test_dict_from_dunder_dict_differs(self):
        """Test if to_dict output differs from __dict__."""
        self.assertNotEqual(self.review.to_dict(), self.review.__dict__)

    def test_with_argument_dict_(self):
        """Test if to_dict method raises TypeError with invalid argument."""
        with self.assertRaises(TypeError):
            self.review.to_dict(None)


if __name__ == "__main__":
    unittest.main()
