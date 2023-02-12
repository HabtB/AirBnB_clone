#!/usr/bin/python4
""" This script serializes instances to a JSON file and
    deserializes JSON files to instances
"""
import datetime
import json
import os


class FileStorage:
    """ This class stores data """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary of objects,.__object"""
        return FileStorage.__objects

    def new(self, obj):
        """Set obj in __objects with key <obj class name>.id"""

        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            obj_dict = {key: value.to_dict()
                        for key, value in FileStorage.__objects.items()}
            json.dump(obj_dict, f)

    def class_names(self):
        """Returns a dictionary of valid classes and their references"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        class_names = {"BaseModel": BaseModel,
                       "User": User,
                       "State": State,
                       "City":City,
                       "Amenity": Amenity,
                       "Place": Place,
                       "Review": Review}

        return class_names

    def reload(self):
        """Reloads the stored objects"""

        if not os.path.isfile(FileStorage.__file_path):
            return

        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)
            obj_dict = {key: self.class_names()[value["__class__"]](**value)
                        for key, value in obj_dict.items()}
            FileStorage.__objects = obj_dict
