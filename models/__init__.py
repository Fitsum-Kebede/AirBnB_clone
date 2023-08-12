#!/usr/bin/python3
"""
Module Description:
The models/__init__.py module serves as the initialization script for
the models package. It creates a unique instance of the FileStorage class,
enabling the entire application to access a single storage mechanism for
serializing and deserializing instances. By calling the reload method during
initialization, this module ensures that any previously stored instances are
loaded into memory, providing continuity and
access to previously created objects.
"""
from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
