#!/usr/bin/python3
""" Unittest module for the class - City"""
import unittest
from models.base_model import BaseModel
from models.city import City
from models.engine.file_storage import FileStorage
from models import storage
import os
import time
from datetime import datetime


class TestUser(unittest.TestCase):
    """ Test cases for the class - City """

    def setUp(self):
        """ Prepares the test methods """
        self.default_state_id = ""
        self.default_city_name = ""

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
        city_instance = City()
        self.assertIsInstance(city_instance, City)
        self.assertTrue(issubclass(type(city_instance), BaseModel))

    def test_user_attributes(self):
        city = City()
        self.assertEqual(city.state_id, self.default_state_id)
        self.assertEqual(city.name, self.default_city_name)

    def test_setting_attributes(self):
        city = City()
        test_state_id = "Test_id_state"
        test_city_name = "Test_city_name"
        city.state_id = test_state_id
        city.name = test_city_name
        self.assertEqual(city.state_id, test_state_id)
        self.assertEqual(city.name, test_city_name)


if __name__ == "__main__":
    unittest.main()
