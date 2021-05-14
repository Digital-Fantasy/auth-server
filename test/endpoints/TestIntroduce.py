import unittest
from start_server import app

class TestEndpointIntroduction(unittest.TestCase):

    def setUp(self):
        """Set up function for tests. This function is run before every test this one runs the flask server in testing mode"""
        app.testing = True
        app.debug = True
        self.app = app.test_client()

    def test_with_data_body(self):
        """Test if a get request to the web server returns status of 200. 200 means all is good."""
        result = self.app.post('/introduction')
        self.assertEqual(result.status_code, 200, "Get of / did not return 200")

if __name__ == '__main__':
    unittest.main()

'''
Test for:
 too short pass reaction
 missing pwd reaction
 missing username reaction
 username already exist reaction
 default variables
 can't parse json
'''