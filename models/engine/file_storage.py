#!/usr/bin/python3
import json
"""
serializes instances to a JSON file
and deserializes JSON file to instances:
"""


class FileStorage():
    """class FileStorage"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        FileStorage.__objects[obj.__class__.__name__ + "." + obj.id] = obj.to_dict()

    def save(self):
        with open(FileStorage.__file_path, "a+") as loadto:
            json.dump(FileStorage.__objects, loadto)

    def reload(self):
        with open(FileStorage.__file_path) as loadfrom:
            FileStorage.__objects = json.load(loadfrom)
