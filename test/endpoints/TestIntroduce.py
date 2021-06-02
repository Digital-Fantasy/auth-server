import unittest
from start_server import app


class TestEndpointIntroductionInvalidRequest(unittest.TestCase):
	
	def setUp(self):
		"""Set up function for tests. This function is run before every test this one runs the flask server in testing mode"""
		app.testing = True
		app.debug = True
		self.app = app.test_client()
	
	def test_with_empty_body(self):
		"""Test sending request with empty body. Should have response code of 400 with response and exception"""
		result = self.app.post('/introduce')
		result_json = result.json
		self.assertIn("exception", result_json, "No exception tag in result that should have exception")
		self.assertIn("response", result_json, "No response tag in result")
		self.assertEqual(result.status_code, 400, "Post of /introduce with no json did not return 400")
		
	def test_with_invalid_body(self):
		"""Test sending request with invalid body. Should have response code of 400 with response and exception"""
		result = self.app.post('/introduce',"}{JsOn Test")
		result_json = result.json
		self.assertIn("exception", result_json, "No exception tag in result that should have exception")
		self.assertIn("response", result_json, "No response tag in result")
		self.assertEqual(result.status_code, 400, "Post of /introduce with invalid json did not return 400")


class TestEndpointIntroductionValid(unittest.TestCase):
	
	def setUp(self):
		"""Set up function for tests. This function is run before every test this one runs the flask server in testing mode"""
		app.testing = True
		app.debug = True
		self.app = app.test_client()
	
	def test_with_empty_body(self):
		"""Test sending request with empty body. Should have response code of 400 with response and exception"""
		result = self.app.post('/introduce', {})
		result_json = result.json
		print(result_json)
		self.assertEqual(result.status_code, 200, "Post of /introduce did not return 200")
	
	def test_with_invalid_body(self):
		"""Test sending request with invalid body. Should have response code of 400 with response and exception"""
		result = self.app.post('/introduce', "}{JsOn Test")
		result_json = result.json
		self.assertEqual(result.status_code, 400, "Get of / did not return 200")

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
