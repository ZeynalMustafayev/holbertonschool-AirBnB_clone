import unittest

from datetime import datetime

from models.engine.file_storage import FileStorage

from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()

    def test_all(self):
        obj = self.__objects
        self.assertNotEqual(x, self.__objects)

    def test_new(self):
        obj = BaseModel()
        key = f"{type(obj).__name__}.{obj.id}"
        self.assertEqual(key, "{BaseModel.{}".format(obj.id))

    def test_save(self):
        obj = BaseModel()
        old_updated_at = obj.updated_at
        self.storage.new(obj)
        self.storage.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at)

    def test_reload(self):
        obj = BaseModel()
        old_updated_at = obj.updated_at
        self.storage.new(obj)
        self.storage.save()
        obj.updated_at = datetime.now()
        self.storage.reload()
        self.assertNotEqual(old_updated_at, obj.updated_at)
