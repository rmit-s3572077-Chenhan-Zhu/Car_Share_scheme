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

#Return 302 means redirect to main index if logout successful
    def test_logout(self):
        result = self.app.get('/logout/')
        self.assertEqual(result.status_code, 302)


if __name__ == '__main__':
    unittest.main()
