import unittest

from datetime import datetime

from models.user import User


class TestUser(unittest.TestCase):
    def setUp(self):
        self.model = User()
        self.model.created_at = datetime.now()
        self.model.updated_at = datetime.now()

    def test_id(self):
        self.model_test = User()
        self.assertNotEqual(self.model.id, self.model_test.id)

    def test_save(self):
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at)
        with open("file.json", "r") as file:
            self.assertIn("User.{}".format(self.model.id), file.read())

    def test_to_dict(self):
        result = self.model.to_dict()
        self.assertEqual(result["__class__"], self.model.__class__.__name__)
        self.assertEqual(result["created_at"], self.model.created_at.isoformat())
        self.assertEqual(result["updated_at"], self.model.updated_at.isoformat())

    def test_str(self):
        expected_str = "[{}] ({}) {}".format(self.model.__class__.__name__, self.model.id, self.model.__dict__)
        self.assertEqual(str(self.model), expected_str)

    def test_email_attr(self):
        user = User()
        self.assertTrue(hasattr(user, "email"))
        self.assertEqual(user.email, "")

    def test_password_attr(self):
        user = User()
        self.assertTrue(hasattr(user, "password"))
        self.assertEqual(user.password, "")

    def test_first_name_attr(self):
        user = User()
        self.assertTrue(hasattr(user, "first_name"))
        self.assertEqual(user.first_name, "")

    def test_last_name_attr(self):
        user = User()
        self.assertTrue(hasattr(user, "last_name"))
        self.assertEqual(user.last_name, "")
