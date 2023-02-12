#!/usr/bin/python3
""" Creates a User class that inherits from the BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """ Defines the class User """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
