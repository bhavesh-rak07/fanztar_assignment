import unittest
import json
from app import app

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_create_order(self):
        # Test with valid data
        response = self.app.post('/orders', json={
            'components': ['I', 'A', 'D', 'F', 'K']
        })
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertIn('order_id', data)
        self.assertIn('total', data)
        self.assertIn('parts', data)
        self.assertEqual(len(data['parts']), 5)

        # Test with invalid data
        response = self.app.post('/orders', json={
            'components': ['A', 'B']
        })
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()
