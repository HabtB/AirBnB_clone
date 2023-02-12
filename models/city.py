#!/usr/bin/python3
""" Creates a City class that inherits from the BaseModel"""
from models.base_model import BaseModel


class City(BaseModel):
    """ Defines the class City """

    state_id = ""
    name = ""
