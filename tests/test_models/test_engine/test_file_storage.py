import unittest

import json

import os

from models.engine.file_storage import FileStorage

from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.file_path = "test_file.json"
        self.objects = {"BaseModel.123": {"id": "123", "name": "test"}}

        with open(self.file_path, "w") as f:
            json.dump(self.objects, f)

    def test_file_path(self):
        storage = FileStorage()
        self.assertEqual(storage._FileStorage__file_path, "file.json")

    def test_all(self):
        storage = FileStorage()
        storage.reload()
        self.assertNotEqual(storage.all(), self.objects)

    def test_new(self):
        obj = BaseModel()
        key = f"{type(obj).__name__}.{obj.id}"
        self.assertEqual(key, "BaseModel.{}".format(obj.id))

    def test_save(self):
        storage = FileStorage()
        storage._FileStorage__file_path = self.file_path
        obj = BaseModel()
        storage.new(obj)
        storage.save()

        with open(self.file_path, "r") as f:
            saved_data = json.load(f)
            self.assertIn("BaseModel." + obj.id, saved_data)

    def test_reload(self):
        storage = FileStorage()
        obj = BaseModel()
        storage.new(obj)
        storage.save()
        storage._FileStorage__objects = {}
        storage.reload()
        self.assertIn('BaseModel.' + obj.id, storage.all())
