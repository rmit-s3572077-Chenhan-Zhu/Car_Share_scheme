import unittest
from zhiliao import login, app
import zhiliao
import flask


class Testmain(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        pass

    # test return information if username or password are invalid
    def test_incorrect_login(self):
        result = self.app.post('/login/', data=dict(username="jinming", password="1234567890"), follow_redirects=True)
        self.assertIn('wrong username or password,please try again', result.data)
    def test_incorrect_login0(self):
        result = self.app.post('/login/', data=dict(username="jiing", password="123"), follow_redirects=True)
        self.assertIn('wrong username or password,please try again', result.data)
    def test_incorrect_login1(self):
        result = self.app.post('/login/', data=dict(username="jinmg", password="12345890"), follow_redirects=True)
        self.assertIn('wrong username or password,please try again', result.data)
    # test login status when login successful
    def test_correct_login(self):
        result = self.app.post('/login/', data=dict(username="jinming", password="123"), follow_redirects=True)
        self.assertEqual(result.status_code, 200)


if __name__ == '__main__':
    unittest.main()
