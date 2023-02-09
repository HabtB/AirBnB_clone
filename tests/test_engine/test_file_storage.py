#!/usr/bin/python3
"""Defines unittests for models/engine/file_storage.py.
Unittest classes:
    TestFileStorage_instantiation
    TestFileStorage_methods
"""

import os
import json
import unittest
from datetime import datetime
from models.engine.file_storage import FileStorage
import models


class TestFileStorageInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the FileStorage class."""

    def test_file_storage_instantiation_no_args(self):
        """Test instantiation with no arguments"""
        self.assertEqual(FileStorage, type(FileStorage()))

    def test_file_storage_instantiation_with_arg(self):
        """Test instantiation with an argument"""
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_path(self):
        """Test that FileStorage has the correct file_path"""
        self.assertTrue(hasattr(FileStorage, "_FileStorage__file_path"))
        self.assertEqual(FileStorage._FileStorage__file_path, "file.json")

    def test_file_storage_file_path_is_private_str(self):
        """Test that FileStorage's file_path is a private string"""
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_file_storage_objects_is_private_dict(self):
        """Test that FileStorage's objects is a private dictionary"""
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_objects(self):
        """Test that FileStorage has the correct __objects"""
        self.assertTrue(hasattr(FileStorage, "_FileStorage__objects"))
        self.assertEqual(type(FileStorage._FileStorage__objects), dict)

    def test_storage_initializes(self):
        """Test that FileStorage initializes correctly"""
        self.assertEqual(type(models.storage), FileStorage)


if __name__ == "__main__":
    unittest.main()
