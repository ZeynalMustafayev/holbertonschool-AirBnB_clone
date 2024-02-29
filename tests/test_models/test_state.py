import unittest

from datetime import datetime

from models.state import State


class TestState(unittest.TestCase):
    def setUp(self):
        self.model = State()
        self.model.created_at = datetime.now()
        self.model.updated_at = datetime.now()

    def test_id(self):
        self.model_test = State()
        self.assertNotEqual(self.model.id, self.model_test.id)

    def test_save(self):
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at)
        with open("file.json", "r") as file:
            self.assertIn("State.{}".format(self.model.id), file.read())

    def test_to_dict(self):
        result = self.model.to_dict()
        self.assertEqual(result["__class__"],
                         self.model.__class__.__name__)
        self.assertEqual(result["created_at"],
                         self.model.created_at.isoformat())
        self.assertEqual(result["updated_at"],
                         self.model.updated_at.isoformat())

    def test_str(self):
        expected_str = "[{}] ({}) {}".format(
            self.model.__class__.__name__, self.model.id, self.model.__dict__)
        self.assertEqual(str(self.model), expected_str)

    def test_name(self):
        state = State()
        self.assertTrue(hasattr(state, "name"))
        self.assertEqual(state.name, "")
