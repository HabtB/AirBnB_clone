#!/usr/bin/python3
""" Unittest module for the class - Amenity"""
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity
from models.engine.file_storage import FileStorage
from models import storage
import os
import time
from datetime import datetime


class TestUser(unittest.TestCase):
    """ Test cases for the class - Amenity """

    def setUp(self):
        """ Prepares the test methods """
        self.default_amenity_name = ""

    def tearDown(self):
        """ Cleans up resources test methods """
        self.resetStorage()
        pass

    def resetStorage(self):
        """ Resets FileStorage data """
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_inheritance(self):
        """ Tests inheritance """
        amenity_instance = Amenity()
        self.assertIsInstance(amenity_instance, Amenity)
        self.assertTrue(issubclass(type(amenity_instance), BaseModel))

    def test_user_attributes(self):
        amenity = Amenity()
        self.assertEqual(amenity.name, self.default_amenity_name)

    def test_setting_attributes(self):
        amenity = Amenity()
        test_amenity_name = "Test_amenity_name"
        amenity.name = test_amenity_name
        self.assertEqual(amenity.name, test_amenity_name)


if __name__ == "__main__":
    unittest.main()
