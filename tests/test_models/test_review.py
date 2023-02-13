#!/usr/bin/python3
""" Unittest module for the class - Review"""
import unittest
from models.base_model import BaseModel
from models.review import Review
from models.engine.file_storage import FileStorage
from models import storage
import os
import time
from datetime import datetime


class TestUser(unittest.TestCase):
    """ Test cases for the class - Review """

    def setUp(self):
        """ Prepares the test methods """
        self.default_place_id = ""
        self.default_user_id = ""
        self.default_text = ""

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
        review_instance = Review()
        self.assertIsInstance(review_instance, Review)
        self.assertTrue(issubclass(type(review_instance), BaseModel))

    def test_user_attributes(self):
        review = Review()
        self.assertEqual(review.place_id, self.default_place_id)
        self.assertEqual(review.user_id, self.default_user_id)
        self.assertEqual(review.text, self.default_text)

    def test_setting_attributes(self):
        review = Review()
        test_place_id = "place_id"
        test_user_id = "user_id"
        test_text = "review_text"
        review.place_id = test_place_id
        review.user_id = test_user_id
        review.text = test_text
        self.assertEqual(review.place_id, test_place_id)
        self.assertEqual(review.user_id, test_user_id)
        self.assertEqual(review.text, test_text)


if __name__ == "__main__":
    unittest.main()
