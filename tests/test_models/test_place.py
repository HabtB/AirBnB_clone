#!/usr/bin/python3
""" Unittest module for the class - Place"""
import unittest
from models.base_model import BaseModel
from models.place import Place
from models.engine.file_storage import FileStorage
from models import storage
import os
import time
from datetime import datetime


class TestUser(unittest.TestCase):
    """ Test cases for the class - Place """

    def setUp(self):
        """ Prepares the test methods """
        self.default_city_id = ""
        self.default_user_id = ""
        self.default_place_name = ""
        self.default_description = ""
        self.default_number_rooms = 0
        self.default_number_bathrooms = 0
        self.default_max_guest = 0
        self.default_price_by_night = 0
        self.default_latitude = 0.0
        self.default_longitude = 0.0
        self.default_amenity_ids = []

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
        place_instance = Place()
        self.assertIsInstance(place_instance, Place)
        self.assertTrue(issubclass(type(place_instance), BaseModel))

    def test_user_attributes(self):
        place = Place()
        self.assertEqual(place.city_id, default_city_id)
        self.assertEqual(place.user_id, default_user_id)
        self.assertEqual(place.name, default_city_name)
        self.assertEqual(place.description, default_description)
        self.assertEqual(place.number_rooms, default_number_rooms)
        self.assertEqual(place.number_bathrooms, default_bath_rooms)
        self.assertEqual(place.max_guest, default_max_guest)
        self.assertEqual(place.price_by_night, default_price_by_night)
        self.assertEqual(place.latitude, default_latitude)
        self.assertEqual(place.longitude, default_longitude)
        self.assertEqual(place.amenity_ids, default_amenity_ids)

    def test_setting_attributes(self):
        place = Place()
        test_city_id = "city_id"
        test_user_id = "user_id"
        test_place_name = "place_name"
        test_description = "description"
        test_number_rooms = 0
        test_number_bathrooms = 0
        test_max_guest = 0
        test_price_by_night = 0
        test_latitude = 0.0
        test_longitude = 0.0
        test_amenity_ids = ["test", "amenity", "id"]
        place.city_id = test_city_id
        place.user_id = test_user_id
        place.name = test_place_name
        place.description = test_description
        place.number_rooms = test_number_rooms
        place.number_bathrooms = test_number_bathrooms
        place.max_guest = test_max_guest
        place.price_by_night = test_price_by_night
        place.latitude = test_latitude
        place.longitude = test_longitude
        place.amenity_ids = test_amenity_ids
        self.assertEqual(place.city_id, test_city_id)
        self.assertEqual(place.user_id, test_user_id)
        self.assertEqual(place.name, test_place_name)
        self.assertEqual(place.description, test_description)
        self.assertEqual(place.number_rooms, test_number_rooms)
        self.assertEqual(place.number_bathrooms, test_number_bathrooms)
        self.assertEqual(place.max_guest, st)
        self.assertEqual(place.price_by_night, test_price_by_night)
        self.assertEqual(place.latitude, test_latitude)
        self.assertEqual(place.longitude, test_longitude)
        self.assertEqual(user.amenity_name, test_amenity_ids)


if __name__ == "__main__":
    unittest.main()
