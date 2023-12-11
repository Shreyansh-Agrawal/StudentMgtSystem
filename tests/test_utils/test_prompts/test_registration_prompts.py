import unittest
from unittest.mock import patch
from utils.prompts import registration_prompts

class TestRegistrationPrompts(unittest.TestCase):
    
    @patch('utils.prompts.registration_prompts.registration_controller')
    @patch('utils.prompts.registration_prompts.course_validation')
    @patch('utils.prompts.registration_prompts.student_validation')
    @patch('utils.prompts.registration_prompts.search_all_courses')
    def test_prompt_add_registration(self, moc_search_all_courses, moc_student_validation, moc_course_validation, moc_registration_controller):
        registration_prompts.prompt_add_registration()
        moc_registration_controller.add_registration.assert_called_once()

    @patch('utils.prompts.registration_prompts.registration_controller')
    @patch('utils.prompts.registration_prompts.student_validation')
    def test_prompt_search_registration(self, moc_student_validation,  moc_registration_controller):
        registration_prompts.prompt_search_registration()
        moc_registration_controller.get_registration.assert_called_once()
    
    @patch('utils.prompts.registration_prompts.registration_controller')
    def test_search_all_registrations(self, moc_registration_controller):
        registration_prompts.search_all_registrations()
        moc_registration_controller.get_all_registrations.assert_called_once()

    @patch('utils.prompts.registration_prompts.course_validation')
    @patch('utils.prompts.registration_prompts.student_controller')
    @patch('utils.prompts.registration_prompts.course_controller')
    @patch('utils.prompts.registration_prompts.student_validation')
    @patch('builtins.input')
    @patch('utils.prompts.registration_prompts.registration_controller')
    def test_prompt_update_registration(self, moc_registration_controller, *mocs):
        registration_prompts.prompt_update_registration()
        moc_registration_controller.update_registration.assert_called_once()

    @patch('utils.prompts.registration_prompts.course_controller')
    @patch('utils.prompts.registration_prompts.course_validation')
    @patch('utils.prompts.registration_prompts.student_controller')
    @patch('utils.prompts.registration_prompts.student_validation')
    @patch('utils.prompts.registration_prompts.registration_controller')
    def test_prompt_delete_registration(self, moc_registration_controller, *mocs):
        registration_prompts.prompt_delete_registration()
        moc_registration_controller.delete_registration.assert_called_once()


if __name__ == '__main__':
    unittest.main()
