#!/usr/bin/python3
"""File storage"""
import json
import os


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        pass

    def all(self):
        return self.__objects

    def new(self, obj):
        key = f"{type(obj).__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        serialized_object = {}
        for key, value in self.__objects.items():
            serialized_object[key] = value.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(serialized_object, f)

    def reload(self):
        from models.base_model import BaseModel
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as f:
                for key, value in json.load(f).items():
                    value = eval(key.split(".")[0])(**value)
                    self.__objects[key] = value
