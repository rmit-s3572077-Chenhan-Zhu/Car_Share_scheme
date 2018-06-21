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

    # ensure that flask was set up correctly, the reason of returning 302 is redirect(if no login).
    def test_index_status_code(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 302)


if __name__ == '__main__':
    unittest.main()
