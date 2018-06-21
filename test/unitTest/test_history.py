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

    def test_incorrect_history(self):

        result = self.app.post('/history/', data=dict(carname="BMW",Btime="8:00AM", Rtime="8:00AM", Bdatetime="1-May",Rdatetime="1-May",),
                               follow_redirects=True)

        #self.assertIn('different passwords,please try again!', result.data)
        #self.assertEqual(result.status_code, 200)

       # Rdatetime = Rdatetime, Bdatetime = Bdatetime, carname = name,
        #Rday = Rday, Rtime = Rtime, Btime = Btime, Bday = Bday)

    def test_correct_history(self):

        result = self.app.post('/history/', data=dict(carname="Volkswagen_Golf",Btime="8:00AM", Rtime="8:00AM", Bdatetime="1-May",Rdatetime="1-May",),
                               follow_redirects=True)
        self.assertEqual(result.status_code, 404)


if __name__ == '__main__':
    unittest.main()
