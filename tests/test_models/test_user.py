#!/usr/bin/python3
""" Unittest module for the class - User"""
import unittest
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage
from models import storage
import os
import time
from datetime import datetime


class TestUser(unittest.TestCase):
    """ Test cases for the class - User """

    def setUp(self):
        """ Prepares the test methods """
        self.default_email = ""
        self.default_password = ""
        self.default_first_name = ""
        self.default_last_name = ""

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
        user_instance = User()
        self.assertIsInstance(user_instance, User)
        self.assertTrue(issubclass(type(user_instance), BaseModel))

    def test_user_attributes(self):
        user = User()
        self.assertEqual(user.email, self.default_email)
        self.assertEqual(user.password, self.default_password)
        self.assertEqual(user.first_name, self.default_first_name)
        self.assertEqual(user.last_name, self.default_last_name)

    def test_setting_attributes(self):
        user = User()
        test_email = "test@example.com"
        test_password = "password"
        test_first_name = "Test"
        test_last_name = "User"
        user.email = test_email
        user.password = test_password
        user.first_name = test_first_name
        user.last_name = test_last_name
        self.assertEqual(user.email, test_email)
        self.assertEqual(user.password, test_password)
        self.assertEqual(user.first_name, test_first_name)
        self.assertEqual(user.last_name, test_last_name)


if __name__ == "__main__":
    unittest.main()
