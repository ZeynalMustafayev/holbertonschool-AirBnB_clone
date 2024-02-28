import unittest
from models.state import State


class TestState(unittest.TestCase):
    def setUp(self):
        self.state = State()

    def test_initialization(self):
        self.assertIsInstance(self.state, State)
        self.assertEqual(self.state.name, "")
        self.assertIsNone(self.state.created_at)
        self.assertIsNone(self.state.updated_at)

    def test_to_dict(self):
        state_dict = self.state.to_dict()
        expected_dict = {
            'id': self.state.id,
            'name': "",
            '__class__': 'State',
            'created_at': self.state.created_at.isoformat(),
            'updated_at': self.state.updated_at.isoformat()
        }
        self.assertDictEqual(state_dict, expected_dict)

    def test_from_dict(self):
        state_dict = {
            'id': '123',
            'name': "Test State",
            'created_at': '2024-02-28T12:00:00',
            'updated_at': '2024-02-28T12:00:00'
        }
        new_state = State(**state_dict)
        self.assertEqual(new_state.id, '123')
        self.assertEqual(new_state.name, "Test State")
        self.assertEqual(new_state.created_at.isoformat(), '2024-02-28T12:00:00')
        self.assertEqual(new_state.updated_at.isoformat(), '2024-02-28T12:00:00')

if __name__ == '__main__':
    unittest.main()

