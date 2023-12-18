import unittest
from unittest.mock import patch

from utils.validations import course_validation

@patch('utils.validations.course_validation.validator', return_value=True)
class TestCourseValidation(unittest.TestCase):
    @patch('builtins.input', return_value='Test Course Name')
    def test_validate_course_name(self, moc_inp, moc_validator):
        result = course_validation.validate_course_name()
        assert result == 'Test Course Name'

    @patch('builtins.input', return_value='Test1001')
    def test_validate_course_id(self, moc_inp, moc_validator):
        result = course_validation.validate_course_id()
        assert result == 'TEST1001'

    @patch('builtins.input', return_value='4')
    def test_validate_course_credits(self, moc_inp, moc_validator):
        result = course_validation.validate_course_credits()
        assert result == '4'
    
    @patch('builtins.input', return_value='Test Discipline')
    def test_validate_course_discipline(self, moc_inp, moc_validator):
        result = course_validation.validate_course_discipline()
        assert result == 'Test Discipline'

    @patch('re.fullmatch', return_value='match obj')
    @patch('utils.validations.course_validation.error_handling')
    def test_validator_success(self, moc_decor, moc_re, moc_validator):
        moc_decor.return_value = lambda x: x
        result = course_validation.validator('test pattern', 'test data')
        assert result is True
    
def demo_deco(func):
    def wrapper(*args, **kwargs):
        print("Inside test decorator")
    return wrapper

class TestValidator(unittest.TestCase):

    @patch('re.fullmatch', return_value=None)
    def test_validator_fail(self, moc_re):
        result = course_validation.validator('test pattern', 'test data')
        assert result is False