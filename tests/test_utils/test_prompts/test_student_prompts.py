import unittest
from unittest.mock import patch
from utils.prompts import student_prompts

class TestStudentPrompts(unittest.TestCase):
    
    @patch('utils.prompts.student_prompts.student_controller')
    @patch('utils.prompts.student_prompts.student_validation')
    def test_prompt_add_student(self, moc_student_validation, moc_student_controller):
        student_prompts.prompt_add_student()
        moc_student_controller.add_student.assert_called_once()

    @patch('utils.prompts.student_prompts.student_controller')
    @patch('utils.prompts.student_prompts.student_validation')
    def test_prompt_search_student(self, moc_student_validation,  moc_student_controller):
        student_prompts.prompt_search_student()
        moc_student_controller.get_student.assert_called_once()
    
    @patch('utils.prompts.student_prompts.student_controller')
    def test_search_all_students(self, moc_student_controller):
        student_prompts.search_all_students()
        moc_student_controller.get_all_students.assert_called_once()

    @patch('utils.prompts.student_prompts.student_validation')
    @patch('builtins.input')
    @patch('utils.prompts.student_prompts.student_controller')
    def test_prompt_update_student(self, moc_student_controller, *mocs):
        student_prompts.prompt_update_student()
        moc_student_controller.update_student.assert_called_once()

    @patch('utils.prompts.student_prompts.student_validation')
    @patch('utils.prompts.student_prompts.student_controller')
    def test_prompt_delete_student(self, moc_student_controller, *mocs):
        student_prompts.prompt_delete_student()
        moc_student_controller.delete_student.assert_called_once()


if __name__ == '__main__':
    unittest.main()
