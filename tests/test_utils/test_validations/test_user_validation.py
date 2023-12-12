import unittest
from unittest.mock import patch, Mock

from utils.validations import user_validation


class TestUserValidations(unittest.TestCase):

    @patch('utils.validations.user_validation.decrypt_password')
    @patch('builtins.input', return_value='test_user')
    @patch('maskpass.askpass', return_value='test_password')
    @patch('utils.validations.user_validation.DatabaseConnection')
    def test_validate_user(self, moc_db_conn, moc_pswd, moc_username, moc_decrypt_password):
        moc_cursor = Mock()
        moc_cursor.fetchall.return_value = [('hashed_pswd', 'admin')]
        moc_connection = Mock()
        moc_connection.cursor.return_value = moc_cursor
        moc_db_conn.return_value.__enter__.return_value = moc_connection
        moc_decrypt_password().decode.return_value = 'test_password'
        result = user_validation.validate_user('admin')
        assert result is True

    @patch('builtins.input', return_value='test role')
    def test_input_user_role(self, moc_inp):
        result = user_validation.input_user_role()
        assert result == 'test role'

    @patch('utils.validations.user_validation.input_user_role', return_value='admin')
    @patch('utils.validations.user_validation.validate_user')
    def test_validate_role(self, moc_inp, moc_validate_user):
        result = user_validation.validate_role()
        assert result == 'admin'
