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
from models.base_model import BaseModel
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


class TestFileStorageMethods(unittest.TestCase):
    """Unittests for testing methods of the FileStorage class."""

    @classmethod
    def setUpClass(cls):
        """
        Set up method for the test class.
        It is called before any tests are run, renames the "file.json" to "tmp"
        to ensure the tests have a clean environment to run in
        """
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tear_down(cls, self):
        """
        Tear down method for the test class.
        It is called after all tests have been run, removes the "file.json",
        renames the "tmp" back to "file.json"
        to restore the file system to its original state.
        """
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_all(self):
        """Test that all() returns the correct dictionary"""
        self.assertEqual(type(models.storage.all()), dict)

    def test_all_with_arg(self):
        """Test all() raises a TypeError when given argument other than None"""
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new_with_args(self):
        """Test new() raises TypeError when given more than one argument"""
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_new(self):
        """Test that new() adds a new object to the dictionary"""
        base_model = BaseModel()
        lenth = len(models.storage.all())
        models.storage.new(base_model)
        self.assertEqual(len(models.storage.all()), lenth + 1)
        self.assertIn("BaseModel." + base_model.id,
                      models.storage.all().keys())
        self.assertIn(base_model, models.storage.all().values())

    def test_save_with_arg(self):
        """Test save() raises TypeError when given argument other than None"""
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_save(self):
        """Test save() correctly serializes the dictionary to a JSON file"""
        base_model = BaseModel()
        models.storage.new(base_model)
        models.storage.save()
        with open("file.json", "r") as file_handle:
            self.assertIn("BaseModel." + base_model.id, file_handle.read())

    def test_reload_with_arg(self):
        """Test reload() raises TypeError if given argument other than None"""
        with self.assertRaises(TypeError):
            models.storage.reload(None)

    def test_reload(self):
        """Test reload() correctly deserializes the JSON file to dictionary"""
        base_model = BaseModel()
        models.storage.new(base_model)
        models.storage.save()
        models.storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + base_model.id, objs)
        self.assertIn("BaseModel." + base_model.id,
                      models.storage.all().keys())
        self.assertIn(base_model.to_dict(), [
                      v.to_dict() for v in models.storage.all().values()])


if __name__ == "__main__":
    unittest.main()
