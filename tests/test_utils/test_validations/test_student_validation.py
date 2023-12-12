import unittest
from unittest.mock import patch

from utils.validations import student_validation


@patch('utils.validations.student_validation.validator', return_value=True)
class TestCourseValidation(unittest.TestCase):

    @patch('builtins.input', return_value='Test Name')
    def test_validate_name(self, moc_inp, moc_validator):
        result = student_validation.validate_name()
        assert result == 'Test Name'

    @patch('builtins.input', return_value='10')
    def test_validate_roll_no(self, moc_inp, moc_validator):
        result = student_validation.validate_roll_no()
        assert result == '10'

    @patch('builtins.input', return_value='18')
    def test_validate_age(self, moc_inp, moc_validator):
        result = student_validation.validate_age()
        assert result == '18'
    
    @patch('builtins.input', return_value='M')
    def test_validate_gender(self, moc_inp, moc_validator):
        result = student_validation.validate_gender()
        assert result == 'M'

    @patch('builtins.input', return_value='8748330973')
    def test_validate_phone(self, moc_re, moc_validator):
        result = student_validation.validate_phone()
        assert result == '8748330973'

    @patch('builtins.input', return_value='2021-01-21')
    def test_validate_date_of_joining(self, moc_re, moc_validator):
        result = student_validation.validate_date_of_joining()
        assert result == '2021-01-21'
