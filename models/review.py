#!/usr/bin/python3
""" Creates a Review class that inherits from the BaseModel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ Defines the class Review """

    place_id = ""
    user_id = ""
    text = ""
