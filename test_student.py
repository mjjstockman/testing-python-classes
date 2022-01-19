import unittest
from student import Student

class TestStudent(unittest.TestCase):

    # class methods run once when class instansiated...
    @classmethod
    def setUpClass(cls):
        print('setUpClass')

    # and once on tear down
    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    def setUp(self):
        print('setUp')
        self.student = Student('Matt', 'Smith')

    def test_full_name(self):
        print('test_full_name')
        self.assertEqual(self.student.full_name, 'Matt Smith')

    def test_email(self):
        print('test_email')
        self.assertEqual(self.student.email, 'matt.smith@email.com')

    def test_alert_santa(self):
        print('test_alert_santa')
        self.student.alert_santa()

        self.assertTrue(self.student.naughty_list)

    
if __name__ == '__main__':
    unittest.main()