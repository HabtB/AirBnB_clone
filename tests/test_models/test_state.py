#!/usr/bin/python3
""" Unittest module for the class - State"""
import unittest
from models.base_model import BaseModel
from models.state import State
from models.engine.file_storage import FileStorage
from models import storage
import os
import time
from datetime import datetime


class TestUser(unittest.TestCase):
    """ Test cases for the class - State """

    def setUp(self):
        """ Prepares the test methods """
        self.default_state_name = ""

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
        state_instance = State()
        self.assertIsInstance(state_instance, State)
        self.assertTrue(issubclass(type(state_instance), BaseModel))

    def test_user_attributes(self):
        state = State()
        self.assertEqual(state.name, self.default_state_name)

    def test_setting_attributes(self):
        state = State()
        test_state_name = "Test_name_state"
        state.name = test_state_name
        self.assertEqual(state.name, test_state_name)


if __name__ == "__main__":
    unittest.main()
