import unittest
from student import Student
from datetime import timedelta

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

    def test_apply_extension(self):
        old_end_date = self.student.end_date
        self.student.apply_extension(10)
        
        self.assertEqual(self.student.end_date, old_end_date + timedelta(days=10))

    
if __name__ == '__main__':
    unittest.main()