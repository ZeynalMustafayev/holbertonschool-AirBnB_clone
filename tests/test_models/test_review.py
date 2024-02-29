import unittest

from datetime import datetime

from models.review import Review


class TestState(unittest.TestCase):
    def setUp(self):
        self.model = Review()
        self.model.created_at = datetime.now()
        self.model.updated_at = datetime.now()

    def test_id(self):
        self.model_test = Review()
        self.assertNotEqual(self.model.id, self.model_test.id)

    def test_save(self):
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at)
        with open("file.json", "r") as file:
            self.assertIn("Review.{}".format(self.model.id), file.read())

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

    def test_place_id(self):
        review = Review()
        self.assertTrue(hasattr(review, "place_id"))
        self.assertEqual(review.place_id, "")

    def test_user_id(self):
        review = Review()
        self.assertTrue(hasattr(review, "user_id"))
        self.assertEqual(review.user_id, "")

    def test_text(self):
        review = Review()
        self.assertTrue(hasattr(review, "text"))
        self.assertEqual(review.text, "")
