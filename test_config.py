import unittest
from zhiliao import login, app
import zhiliao
from flask import json


class Testmain(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        pass

    # test whether config data was set up successful
    def testConfig(self):
        self.assertFalse(app.config['SQLALCHEMY_DATABASE_URI'] is '12345')
        self.assertFalse(app.config['SECRET_KEY'] is 'my_precious')
        self.assertTrue(app.config['DEBUG'] is True)


if __name__ == '__main__':
    unittest.main()
