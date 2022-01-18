import unittest
from student import Student

class TestStudent(unittest.TestCase):

    def test_full_name(self):
        # create instance of Student with correct args
        student = Student('Matt', 'Smith')

        self.assertEqual(student.full_name, 'Matt Smith')

    def test_alert_santa(self):
        student = Student('Matt', 'Smith')
        student.alert_santa()

        self.assertTrue(student.naughty_list)

    def test_email(self):
        student = Student('Matt', 'Smith')

        self.assertEqual(student.email, 'matt.smith@email.com')



if __name__ == '__main__':
    unittest.main()