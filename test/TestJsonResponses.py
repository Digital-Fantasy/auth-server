import unittest
import json
from start_server import app

endpoints = ['/introduce']

class TestGetAndPostValidJsonResponse(unittest.TestCase):

    def setUp(self):
        """Set up function for tests. This function is run before every test this one runs the flask server in testing mode"""
        app.testing = True
        app.debug = True
        self.app = app.test_client()

    def test_get_valid_json(self):
        """Test if is_json is true on the response of a request"""
        for endpoint in endpoints:
            result = self.app.get(endpoint)
            self.assertTrue(result.is_json)

    def test_post_valid_json(self):
        """Test if is_json is true on the response of a request"""
        for endpoint in endpoints:
            result = self.app.post(endpoint)
            print(result)
            self.assertTrue(result.is_json)

    def test_get_json_response(self):
        """Test if there is a response key in the response"""
        for endpoint in endpoints:
            result = self.app.get(endpoint)
            self.assertTrue(result.is_json)

    def test_get_json_in_content_type(self):
        """Sees if there is json in the context headers"""
        for endpoint in endpoints:
            response = self.app.get(endpoint)
            self.assertIn("json",response.content_type)

    def test_post_json_in_content_type(self):
        """Sees if there is json in the context headers"""
        for endpoint in endpoints:
            response = self.app.post(endpoint)
            print("response")
            print(response.content_type)
            self.assertIn("json", response.content_type)

    def test_post_json_response_in_response(self):
        """Test if response is_json is True and response in keys"""
        for endpoint in endpoints:
            result = self.app.post(endpoint)
            self.assertTrue(result.is_json)
            response = result.json
            self.assertIn("response",response.keys())

    def test_get_json_response_in_response(self):
        """Is there a response tag in the json response"""
        for endpoint in endpoints:
            response = self.app.get(endpoint)
            response = response.get_json(force=True)
            self.assertIn("response", response.keys())

    def test_post_json_response_in_response(self):
        """Is there a response tag in the json response"""
        for endpoint in endpoints:
            response = self.app.get(endpoint)
            response = response.get_json(force=True)
            self.assertIn("response", response.keys())



if __name__ == '__main__':
    unittest.main()