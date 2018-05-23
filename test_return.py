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
    def test_incorrct_return(self):
        result=self.app.post()
















if __name__ == '__main__':
    unittest.main()
