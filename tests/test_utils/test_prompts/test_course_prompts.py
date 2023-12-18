import unittest
from unittest.mock import patch
from utils.prompts import course_prompts

class TestCoursePrompts(unittest.TestCase):
    
    @patch('utils.prompts.course_prompts.course_controller')
    @patch('utils.prompts.course_prompts.course_validation')
    def test_prompt_add_course(self, moc_course_validation,  moc_course_controller):
        course_prompts.prompt_add_course()
        moc_course_controller.add_course.assert_called_once()
    
    @patch('utils.prompts.course_prompts.course_controller')
    @patch('utils.prompts.course_prompts.course_validation')
    def test_prompt_add_course_value_err(self, moc_course_validation,  moc_course_controller):
        moc_course_validation.validate_course_credits.return_value = 'string_value'
        course_prompts.prompt_add_course()
        moc_course_controller.add_course.assert_not_called()

    @patch('utils.prompts.course_prompts.course_controller')
    @patch('utils.prompts.course_prompts.course_validation')
    def test_prompt_search_course(self, moc_course_validation,  moc_course_controller):
        course_prompts.prompt_search_course()
        moc_course_controller.get_course.assert_called_once()
    
    @patch('utils.prompts.course_prompts.course_controller')
    def test_search_all_courses(self,  moc_course_controller):
        course_prompts.search_all_courses()
        moc_course_controller.get_all_courses.assert_called_once()

    @patch('utils.prompts.course_prompts.course_controller')
    @patch('utils.prompts.course_prompts.course_validation')
    @patch('builtins.input')
    def test_prompt_update_course(self, moc_inp, moc_course_validation,  moc_course_controller):
        course_prompts.prompt_update_course()
        moc_course_controller.update_course.assert_called_once()

    @patch('utils.prompts.course_prompts.course_controller')
    @patch('utils.prompts.course_prompts.course_validation')
    def test_prompt_delete_course(self, moc_course_validation,  moc_course_controller):
        course_prompts.prompt_delete_course()
        moc_course_controller.delete_course.assert_called_once()


if __name__ == '__main__':
    unittest.main()