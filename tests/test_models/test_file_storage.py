#!/usr/bin/python3
"""This module defines unit test for FileStorage class"""
import unittest
from models.engine.file_storage import FileStorage
from models import storage
from datetime import datetime


class Test_FileStorage(unittest.TestCase):
    """ test for implementing the FileStorage class and integrating
    it with the existing classes
    """
    def test_Initialization_and_Reload(self):
        s_instance = FileStorage()
        s_instance.reload()
        return_type = s_instance.all()
        self.assertEqual(type(return_type), dict)
