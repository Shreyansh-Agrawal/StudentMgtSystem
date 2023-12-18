import unittest
from unittest.mock import MagicMock, patch
import sqlite3
from controllers.registration_controller import (
    create_registration_table,
    add_registration,
    get_registration,
    get_all_registrations,
    update_registration,
    delete_registration,
)

class TestRegistrationFunctions(unittest.TestCase):

    def test_create_registration_table(self):
        with patch('controllers.registration_controller.DatabaseConnection') as mock_db_connection:
            mock_cursor = MagicMock()
            mock_db_connection.return_value.__enter__.return_value.cursor.return_value = mock_cursor

            create_registration_table()

            mock_cursor.execute.assert_called()

    def test_add_registration(self):
        with patch('controllers.registration_controller.DatabaseConnection') as mock_db_connection:
            mock_cursor = MagicMock()
            mock_db_connection.return_value.__enter__.return_value.cursor.return_value = mock_cursor

            add_registration(123, 'CS101', '2023-01-01')

            mock_cursor.execute.assert_called()

    def test_add_registration_integrity_err(self):
        with patch('controllers.registration_controller.DatabaseConnection') as mock_db_connection:
            mock_cursor = MagicMock()
            mock_db_connection.return_value.__enter__.return_value.cursor.return_value = mock_cursor
            mock_cursor.execute.side_effect = sqlite3.IntegrityError
            add_registration(123, 'CS101', '2023-01-01')

            mock_cursor.execute.assert_called()

    def test_add_registration_operational_err(self):
        with patch('controllers.registration_controller.DatabaseConnection') as mock_db_connection:
            mock_cursor = MagicMock()
            mock_db_connection.return_value.__enter__.return_value.cursor.return_value = mock_cursor
            mock_cursor.execute.side_effect = sqlite3.OperationalError
            add_registration(123, 'CS101', '2023-01-01')

            mock_cursor.execute.assert_called()

    def test_get_registration(self):
        with patch('controllers.registration_controller.DatabaseConnection') as mock_db_connection:
            mock_cursor = MagicMock()
            mock_cursor.fetchall.return_value = [(123, 'CS101', '2023-01-01')]
            mock_db_connection.return_value.__enter__.return_value.cursor.return_value = mock_cursor

            registration = get_registration(123)

            self.assertEqual(len(registration), 1)
            self.assertEqual(registration[0]['course_id'], 'CS101')


    def test_get_all_registrations(self):
        with patch('controllers.registration_controller.DatabaseConnection') as mock_db_connection:
            mock_cursor = MagicMock()
            mock_cursor.fetchall.return_value = [(123, 'John Doe', 'CS101', 'Computer Science', '2023-01-01')]
            mock_db_connection.return_value.__enter__.return_value.cursor.return_value = mock_cursor

            registrations = get_all_registrations()

            self.assertEqual(len(registrations), 1)
            self.assertEqual(registrations[0]['name'], 'John Doe')

    def test_update_registration(self):
        with patch('controllers.registration_controller.DatabaseConnection') as mock_db_connection:
            mock_cursor = MagicMock()
            mock_db_connection.return_value.__enter__.return_value.cursor.return_value = mock_cursor

            update_registration(123, 'CS101', 'CS102')

            mock_cursor.execute.assert_called()

    def test_update_registration_integrity_err(self):
        with patch('controllers.registration_controller.DatabaseConnection') as mock_db_connection:
            mock_cursor = MagicMock()
            mock_db_connection.return_value.__enter__.return_value.cursor.return_value = mock_cursor
            mock_cursor.execute.side_effect = sqlite3.IntegrityError

            update_registration(123, 'CS101', 'CS102')

            mock_cursor.execute.assert_called()

    def test_update_registration_operational_err(self):
        with patch('controllers.registration_controller.DatabaseConnection') as mock_db_connection:
            mock_cursor = MagicMock()
            mock_db_connection.return_value.__enter__.return_value.cursor.return_value = mock_cursor
            mock_cursor.execute.side_effect = sqlite3.OperationalError

            update_registration(123, 'CS101', 'CS102')

            mock_cursor.execute.assert_called()

    def test_delete_registration(self):
        with patch('controllers.registration_controller.DatabaseConnection') as mock_db_connection:
            mock_cursor = MagicMock()
            mock_db_connection.return_value.__enter__.return_value.cursor.return_value = mock_cursor

            delete_registration(123, 'CS101')

            mock_cursor.execute.assert_called()

    def test_delete_registration_integrity_err(self):
        with patch('controllers.registration_controller.DatabaseConnection') as mock_db_connection:
            mock_cursor = MagicMock()
            mock_db_connection.return_value.__enter__.return_value.cursor.return_value = mock_cursor
            mock_cursor.execute.side_effect = sqlite3.IntegrityError

            delete_registration(123, 'CS101')

            mock_cursor.execute.assert_called()

    def test_delete_registration_operational_err(self):
        with patch('controllers.registration_controller.DatabaseConnection') as mock_db_connection:
            mock_cursor = MagicMock()
            mock_db_connection.return_value.__enter__.return_value.cursor.return_value = mock_cursor
            mock_cursor.execute.side_effect = sqlite3.OperationalError

            delete_registration(123, 'CS101')

            mock_cursor.execute.assert_called()


if __name__ == '__main__':
    unittest.main()
