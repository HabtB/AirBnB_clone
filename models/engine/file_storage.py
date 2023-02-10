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
            obj_dict = {k: v.to_dict()
                        for k, v in FileStorage.__objects.items()}
            json.dump(obj_dict, f)

    def class_def(self):
        """Returns a dictionary of valid classes and their references"""
        from models.base_model import BaseModel

        class_def = {"BaseModel": BaseModel}
        return class_def

    def reload(self):
        """Reloads the stored objects"""

        if not os.path.isfile(FileStorage.__file_path):
            return

        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)
            obj_dict = {k: self.class_def()[v["__class__"]](**v)
                        for k, v in obj_dict.items()}
            FileStorage.__objects = obj_dict
