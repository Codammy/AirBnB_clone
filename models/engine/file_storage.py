#!/usr/bin/pthon3
"""module bears FileStorage"""
import json
from datetime import datetime


class FileStorage:
    """class FileStorage that serializes instances to a
    JSON file and deserializes JSON file to instances"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """returns the dictionart __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets __objects"""
        FileStorage.__objects[f"{obj['__class__']}.{obj['id']}"] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path"""
        with open(FileStorage.__file_path, "w") as s:
            json.dump(FileStorage.__objects, s)

    def reload(self):
        """deserializes the JSON file only if the JSON file exists"""
        try:
            with open(FileStorage.__file_path) as d:
                FileStorage.__objects = json.load(d)
        finally:
            pass
