import unittest
from zhiliao import login,app
import zhiliao
import flask

class Testmain(unittest.TestCase):


    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        pass

    # test return infomation if username or password are invalid
    def test_incorrect_register(self):
        result = self.app.post('/register/', data=dict(username="jingming", password1="123" , password2="1234567899" ), follow_redirects=True)
        self.assertIn('different passwords,please try again!',result.data)

    # test register status when successful
    def test_correct_register(self):
        result = self.app.post('/register/', data=dict(username="jingming", password1="123", password2="123"),
                               follow_redirects=True)
        self.assertEqual(result.status_code, 200)

if __name__ =='__main__':
    unittest.main()
