import unittest
import os
import sqlite3
from controllers.course_controller import create_course_table, add_course, get_course

class TestCourseFunctions(unittest.TestCase):

    def setUp(self):
        self.test_db_name = 'test_data.db'
        self.connection = sqlite3.connect(self.test_db_name)
        self.cursor = self.connection.cursor()
        create_course_table()

    def tearDown(self):
        self.connection.close()
        os.remove(self.test_db_name)

    def test_add_course(self):
        add_course('CS101', 'Computer Science', 3, 'Computer Science', '2023-01-01')
        course = get_course('CS101')
        self.assertEqual(len(course), 1)
        self.assertEqual(course[0]['course_name'], 'Computer Science')

    def test_get_course(self):
        add_course('ENG101', 'English', 3, 'Language', '2023-01-01')
        course = get_course('ENG101')
        self.assertEqual(len(course), 1)
        self.assertEqual(course[0]['course_discipline'], 'Language')

if __name__ == '__main__':
    unittest.main()
