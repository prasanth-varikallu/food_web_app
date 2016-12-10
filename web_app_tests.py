# imports
from food_webapp import app  # import the server application
import unittest  # import the unittest module
import os

class AppTestCase(unittest.TestCase):

	def test_server_response(self):
		tester = app.test_client(self)
		response = tester.get('/', content_type = 'html/text')
		self.assertEqual(response.status_code, 404)

	def test_database(self):
		tester = os.path.exists('food_app.db')
		self.assertTrue(tester)

if __name__ == '__main__':
	unittest.main()