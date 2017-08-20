import os
import unittest
from project import app, db

TEST_DB = 'user.db'

class ProjectTests(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()

        self.assertEquals(app.debug, False)

    def tearDown(self):
        pass

    def test_login_page(self):
        response = self.app.get('/login', follow_redirects=True)
        self.assertIn(b'Future site for logging into Kennedy Family Recipes!', response.data)




if __name__ == '__main__':
    unittest.main()