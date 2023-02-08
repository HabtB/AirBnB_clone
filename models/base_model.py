#!/usr/bin/python3
"""A base class, BaseModel, for the AirBnB project """


from datetime import datetime
import uuid


class BaseModel:
    """This defines the base class from which all other classes inherit"""

    def __init__(self, *args, **kwargs):
        """ instantiates objects of the class BaseModel """

        time_format = "%Y-%m-%dT%H:%M:%S.%f"

        if kwargs:
            for key, value in kwargs.items():
                if key == 'updated_at':
                    self.updated_at = datetime.strptime(value, time_format)
                elif key == 'created_at':
                    self.created_at = datetime.strptime(value, time_format)
                elif key != "__class__":
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        return f'{self.__class__.__name__} {self.id} {self.__dict__}'

    def save(self):
        """ updates the time when it object gets updated """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ returns the .__dict__ values of all instances created"""
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
