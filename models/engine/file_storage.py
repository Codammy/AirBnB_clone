#!/usr/bin/python3
import json
""" class FileStorage that serializes instances to a JSON file and deserializes JSON file to instances:

    models/engine/file_storage.py"""

class FileStorage():
    """class FileStorage"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return __objects

    def new(self, obj):
        obj.__class__.name 

    def save(self):
        with open(__file_path, "w+") as tosave:
            json.dump(__objects)

    def reload(self):
        with open(__file_path, "r") as tosave:
            return json.load(__objects)
