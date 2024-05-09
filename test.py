import unittest
from app import app 


class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app
        self.client = self.app.test_client()

    def test_get_index(self):
        response = self.client.get('/', query_string={'key': 'some_key'})
        self.assertEqual(response.status_code, 200)
    def test_post_index(self):
        response = self.client.post('/', data={'key': 'some_key', 'value': 'some_value'})
        self.assertEqual(response.status_code, 201) 

    def test_put_index(self):
        response = self.client.put('/', data={'key': 'some_key', 'value': 'new_value'})
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
