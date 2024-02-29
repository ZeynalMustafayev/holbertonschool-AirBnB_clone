import unittest

from datetime import datetime

from models.place import Place


class TestPlace(unittest.TestCase):
    def setUp(self):
        self.model = Place()
        self.model.created_at = datetime.now()
        self.model.updated_at = datetime.now()

    def test_id(self):
        self.model_test = Place()
        self.assertNotEqual(self.model.id, self.model_test.id)

    def test_save(self):
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at)
        with open("file.json", "r") as file:
            self.assertIn("Place.{}".format(self.model.id), file.read())

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

    def test_name_attr(self):
        place = Place()
        self.assertTrue(hasattr(place, "name"))
        self.assertEqual(place.name, "")

    def test_city_id_attr(self):
        city = Place()
        self.assertTrue(hasattr(city, "city_id"))
        self.assertEqual(city.city_id, "")

    def test_user_id_attr(self):
        city = Place()
        self.assertTrue(hasattr(city, "user_id"))
        self.assertEqual(city.user_id, "")

    def test_description_attr(self):
        city = Place()
        self.assertTrue(hasattr(city, "description"))
        self.assertEqual(city.description, "")

    def test_number_rooms_attr(self):
        city = Place()
        self.assertTrue(hasattr(city, "number_rooms"))
        self.assertEqual(city.number_rooms, 0)

    def test_number_bathrooms_attr(self):
        city = Place()
        self.assertTrue(hasattr(city, "number_bathrooms"))
        self.assertEqual(city.number_bathrooms, 0)

    def test_max_guest_attr(self):
        city = Place()
        self.assertTrue(hasattr(city, "max_guest"))
        self.assertEqual(city.max_guest, 0)

    def test_price_by_night_attr(self):
        city = Place()
        self.assertTrue(hasattr(city, "price_by_night"))
        self.assertEqual(city.price_by_night, 0)

    def test_latitude_attr(self):
        city = Place()
        self.assertTrue(hasattr(city, "latitude"))
        self.assertEqual(city.latitude, 0.0)

    def test_longitude_attr(self):
        city = Place()
        self.assertTrue(hasattr(city, "longitude"))
        self.assertEqual(city.longitude, 0.0)

    def test_amenity_ids_attr(self):
        city = Place()
        self.assertTrue(hasattr(city, "amenity_ids"))
        self.assertEqual(city.amenity_ids, [])
