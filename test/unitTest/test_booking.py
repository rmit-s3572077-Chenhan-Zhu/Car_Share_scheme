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
    def test_incorrect_booking(self):
        result =self.app.post('/booking/', data=dict(name="316i", price="145",brand="BMW",bluetooth="bluetooth",seat="5",vehicleType="economic",username="jinming",kilometer="150000"),
                               follow_redirects=True)
        #self.assertEqual(result.status_code, 302)
    def test_correct_booking(self):
        result = self.app.post('/booking/', data=dict(name="316i", price="145",brand="BMW",bluetooth="bluetooth",seat="5",vehicleType="luxury",username="jinming",kilometer="150000"),
                               follow_redirects=True)
        self.assertEqual(result.status_code, 200)





if __name__ == '__main__':
            unittest.main()