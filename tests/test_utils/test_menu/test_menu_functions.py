import unittest
from unittest.mock import patch

from utils.menu.menu_functions import (course_menu, registration_menu,
                                       student_menu)

class TestMenu(unittest.TestCase):

    @patch('utils.menu.menu_functions.student_prompts')
    @patch('builtins.input', side_effect=['1', '2', '3', '4', '5', '6', 'q'])
    def test_student_menu(self, moc_inp, moc_student_prompts):
        student_menu()

        moc_student_prompts.prompt_add_student.assert_called_once()
        moc_student_prompts.prompt_search_student.assert_called_once()
        moc_student_prompts.search_all_students.assert_called_once()
        moc_student_prompts.prompt_update_student.assert_called_once()
        moc_student_prompts.prompt_delete_student.assert_called_once()

    @patch('utils.menu.menu_functions.course_prompts')
    @patch('builtins.input', side_effect=['1', '2', '3', '4', '5', '6', 'q'])
    def test_course_menu(self, moc_inp, moc_student_prompts):
        course_menu()

        moc_student_prompts.prompt_add_course.assert_called_once()
        moc_student_prompts.prompt_search_course.assert_called_once()
        moc_student_prompts.search_all_courses.assert_called_once()
        moc_student_prompts.prompt_update_course.assert_called_once()
        moc_student_prompts.prompt_delete_course.assert_called_once()

    @patch('utils.menu.menu_functions.registration_prompts')
    @patch('builtins.input', side_effect=['1', '2', '3', '4', '5', '6', 'q'])
    def test_registration_menu(self, moc_inp, moc_student_prompts):
        registration_menu()

        moc_student_prompts.prompt_add_registration.assert_called_once()
        moc_student_prompts.prompt_search_registration.assert_called_once()
        moc_student_prompts.search_all_registrations.assert_called_once()
        moc_student_prompts.prompt_update_registration.assert_called_once()
        moc_student_prompts.prompt_delete_registration.assert_called_once()


if __name__ == '__main__':
    unittest.main()
