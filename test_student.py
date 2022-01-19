import unittest
from student import Student
from datetime import timedelta
from unittest.mock import patch

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

    def test_course_schedule_success(self):
        # create obj named mocked_get to mock API functionailty
        with patch("student.requests.get") as mocked_get:
            # mock the values
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"

            schedule = self.student.course_schedule()
            self.assertEqual(schedule, "Success")

    def test_course_schedule_failed(self):
        # create obj named mocked_get to mock API functionailty
        with patch("student.requests.get") as mocked_get:
            # mock the values
            mocked_get.return_value.ok = False

            schedule = self.student.course_schedule()
            self.assertEqual(schedule, "Something went wrong")
            

    
if __name__ == '__main__':
    unittest.main()