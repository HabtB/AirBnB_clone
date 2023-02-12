# #!/usr/bin/python3
# """Defines unittests for the User class in models/user.py
# """
# import unittest
# from models.base_model import BaseModel
# from models.user import User


# class TestUser(unittest.TestCase):
#     """Contains unittests for testing the User class

#     The tests cover the attributes and their types, the presence of the
#     attributes, the default values of the attributes, and the ability to set
#     the attributes.
#     """

#     def setUp(self):
#         self.user = User()

#     def test_user_attributes_type(self):
#         """Test the attributes of the User class are of the correct type"""
#         self.assertIsInstance(self.user, BaseModel)
#         self.assertIsInstance(self.user.email, str)
#         self.assertIsInstance(self.user.password, str)
#         self.assertIsInstance(self.user.first_name, str)
#         self.assertIsInstance(self.user.last_name, str)

#     def test_attributes(self):
#         """Test that the User class has the correct attributes"""
#         self.assertTrue(hasattr(self.user, "email"))
#         self.assertTrue(hasattr(self.user, "password"))
#         self.assertTrue(hasattr(self.user, "first_name"))
#         self.assertTrue(hasattr(self.user, "last_name"))

#     def test_values_defaults(self):
#         """Test that the default values of the attributes are correct"""
#         self.assertEqual(
#             self.user.email, "")  # default value "" for email attribute
#         # default value "" for password attribute
#         self.assertEqual(self.user.password, "")
#         # default value "" for first_name attribute
#         self.assertEqual(self.user.first_name, "")
#         # default value "" for last_name attribute
#         self.assertEqual(self.user.last_name, "")

#     def test_user_set_attributes(self):
#         """Test that the attributes of the User class can be set"""
#         user = User()
#         user.email = "test@example.com"
#         user.password = "password"
#         user.first_name = "John"
#         user.last_name = "Doe"
#         self.assertEqual(user.email, "test@example.com")
#         self.assertEqual(user.password, "password")
#         self.assertEqual(user.first_name, "John")
#         self.assertEqual(user.last_name, "Doe")


# if __name__ == '__main__':
#     unittest.main()
