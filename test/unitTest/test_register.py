 /* Author: Jinming Liu */ 
        
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
    def test_incorrect_register(self):
        result = self.app.post('/register/', data=dict(username="jinming", password1="123", password2="1234567899"),
                               follow_redirects=True)
        self.assertIn('different passwords,please try again!', result.data)

    def test_incorrect_register0(self):
        result = self.app.post('/register/', data=dict(username="jinmg", password1="123", password2="123"),
                               follow_redirects=True)
       # self.assertIn('wrong username or password,please try again!', result.data)


    def test_incorrect_register1(self):
        result = self.app.post('/register/', data=dict(username="jinmg", password1="123", password2="123899"),
                               follow_redirects=True)
        #self.assertIn('wrong username and password,please try again!', result.data)

    # test regiter status when successful
    def test_correct_register(self):
        result = self.app.post('/register/', data=dict(username="jinming", password1="123", password2="123"),
                               follow_redirects=True)
        self.assertEqual(result.status_code, 200)


if __name__ == '__main__':
    unittest.main()
