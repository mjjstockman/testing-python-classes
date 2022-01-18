import unittest
from student import Student

class TestStudent(unittest.TestCase):

    def test_full_name(self):
        # create instance of Student with correct args
        student = Student('Matt', 'Smith')

        self.assertEqual(student.full_name, 'Matt Smith')


if __name__ == '__main__':
    unittest.main()