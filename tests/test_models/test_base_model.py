#!/usr/bin/python3
"""Defines unittests for models/base_model.py.
Unittest classes:
    TestBaseModel_instantiation
    TestBaseModel_save
    TestBaseModel_to_dict
"""
import os
import unittest
from datetime import datetime
import models
from time import sleep
from models.base_model import BaseModel


class TestBaseModelInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the BaseModel class."""

    def test_no_args_instantiates(self):
        """Test instantiation of the BaseModel class with no arguments."""
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_id_is_uuid(self):
        """Test that the id attribute is a uuid."""
        base_model = BaseModel()
        uuid = base_model.id
        self.assertEqual(4, uuid.count("-"))
        uuid = uuid.replace("-", "")
        self.assertEqual(32, len(uuid))
        self.assertEqual(int, type(int(uuid, 16)))

    def test_created_at_is_datetime(self):
        """Test that the created_at attribute is a datetime."""
        base_model = BaseModel()
        self.assertEqual(datetime, type(base_model.created_at))

    def test_updated_at_is_datetime(self):
        """Test that the updated_at attribute is a datetime."""
        base_model = BaseModel()
        self.assertEqual(datetime, type(base_model.updated_at))

    def test_id_is_public_str(self):
        """Test that the id attribute is a public instance of type str."""
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_public_datetime(self):
        """Test created_at attribute is a public instance of type datetime"""
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_public_datetime(self):
        """Test updated_at attribute is a public instance of type datetime"""
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_two_models_unique_ids(self):
        """Test that two BaseModel instances have different ids."""
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

    def test_two_models_unique_created_at(self):
        """Test two BaseModel instances have different created_at values"""
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.created_at, bm2.created_at)

    def test_two_models_unique_updated_at(self):
        """Test two BaseModel instances have different updated_at values"""
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.updated_at, bm2.updated_at)

    def test_args_unused(self):
        """Test that args are unused."""
        base_model = BaseModel(None)
        self.assertNotIn(None, base_model.__dict__.values())

    def test_instantiation_with_none_kwargs(self):
        """Test a BaseModel instance can be instantiated with None kwargs"""
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_kwargs_instantiates(self):
        """Test a BaseModel instance can be instantiated with kwargs"""
        base_model = BaseModel(id="123",
                               created_at="2020-06-29T21:30:00.000000",
                               updated_at="2020-06-29T21:30:00.000000")
        self.assertEqual("123", base_model.id)
        self.assertEqual(datetime(2020, 6, 29, 21, 30, 0, 0),
                         base_model.created_at)
        self.assertEqual(datetime(2020, 6, 29, 21, 30, 0, 0),
                         base_model.updated_at)

    def test_instantiation_with_kwargs(self):
        """Test a BaseModel instance can be instantiated with kwargs"""
        date_time = datetime.today()
        dt_iso = date_time.isoformat()
        base_model = BaseModel(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(base_model.id, "345")
        self.assertEqual(base_model.created_at, date_time)
        self.assertEqual(base_model.updated_at, date_time)

    def test_instantiation_with_args_and_kwargs(self):
        """Test BaseModel instance can be instantiated with args and kwargs"""
        date_time = datetime.today()
        dt_iso = date_time.isoformat()
        base_model = BaseModel(
            "12", id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(base_model.id, "345")
        self.assertEqual(base_model.created_at, date_time)
        self.assertEqual(base_model.updated_at, date_time)

    # def test_new_instance_stored_in_objects(self):
    #     """Test new instance of BaseModel is properly stored in __objects"""
    #     self.assertIn(BaseModel(), models.storage.all().values())


class TestBaseModelSave(unittest.TestCase):
    """Unittests for testing save method of the BaseModel class."""

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

    def test_one_save(self):
        """Test the save method updates the updated_at of BaseModel instance"""
        base_model = BaseModel()
        sleep(0.05)
        first_updated_at = base_model.updated_at
        base_model.save()
        self.assertLess(first_updated_at, base_model.updated_at)

    def test_two_saves(self):
        """Test the save method updates the updated_at of BaseModel instance"""
        base_model = BaseModel()
        sleep(0.05)
        first_updated_at = base_model.updated_at
        base_model.save()
        sleep(0.05)
        second_updated_at = base_model.updated_at
        base_model.save()
        self.assertLess(first_updated_at, second_updated_at)
        self.assertLess(second_updated_at, base_model.updated_at)

    # def test_save_with_arg(self):
    #     """Test that the save method does not accept any arguments."""
    #     base_model = BaseModel()
    #     with self.assertRaises(TypeError):
    #         base_model.save(None)

    # def test_save_updates_file(self):
    #     """Test that the save method updates the file.json file."""
    #     base_model = BaseModel()
    #     base_model.save()
    #     print(os.path.abspath("file.json"))
    #     with open("file.json", "r", encoding="utf-8") as file_handle:
    #         self.assertIn(base_model.id, file_handle.read())


if __name__ == "__main__":
    unittest.main()
