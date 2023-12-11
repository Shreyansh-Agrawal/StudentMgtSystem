import unittest
from unittest.mock import MagicMock, patch
from controllers.student_controller import (
    create_students_table,
    add_student,
    get_student,
    get_all_students,
    update_student,
    delete_student,
)


class TestStudentFunctions(unittest.TestCase):
    def test_create_students_table(self):
        with patch(
            "controllers.student_controller.DatabaseConnection"
        ) as mock_db_connection:
            mock_cursor = MagicMock()
            mock_db_connection.return_value.__enter__.return_value.cursor.return_value = (
                mock_cursor
            )

            create_students_table()

            mock_cursor.execute.assert_called()

    def test_add_student(self):
        with patch(
            "controllers.student_controller.DatabaseConnection"
        ) as mock_db_connection:
            mock_cursor = MagicMock()
            mock_db_connection.return_value.__enter__.return_value.cursor.return_value = (
                mock_cursor
            )

            add_student(
                123, "John Doe", 20, "Male", "1234567890", "2023-01-01", "2023-01-01"
            )

            mock_cursor.execute.assert_called()

    def test_get_student(self):
        with patch(
            "controllers.student_controller.DatabaseConnection"
        ) as mock_db_connection:
            mock_cursor = MagicMock()
            mock_cursor.fetchall.return_value = [
                (123, "John Doe", 20, "Male", "1234567890", "2023-01-01", "2023-01-01")
            ]
            mock_db_connection.return_value.__enter__.return_value.cursor.return_value = (
                mock_cursor
            )

            student = get_student(123)

            self.assertEqual(len(student), 1)
            self.assertEqual(student[0]["name"], "John Doe")

    def test_get_all_students(self):
        with patch(
            "controllers.student_controller.DatabaseConnection"
        ) as mock_db_connection:
            mock_cursor = MagicMock()
            mock_cursor.fetchall.return_value = [
                (123, "John Doe", 20, "Male", "1234567890", "2023-01-01", "2023-01-01")
            ]
            mock_db_connection.return_value.__enter__.return_value.cursor.return_value = (
                mock_cursor
            )

            students = get_all_students()

            self.assertEqual(len(students), 1)
            self.assertEqual(students[0]["roll_no"], 123)

    def test_update_student(self):
        with patch(
            "controllers.student_controller.DatabaseConnection"
        ) as mock_db_connection:
            mock_cursor = MagicMock()
            mock_db_connection.return_value.__enter__.return_value.cursor.return_value = (
                mock_cursor
            )

            update_student(123, "Jane Doe")

            mock_cursor.execute.assert_called()

    def test_delete_student(self):
        with patch(
            "controllers.student_controller.DatabaseConnection"
        ) as mock_db_connection:
            mock_cursor = MagicMock()
            mock_db_connection.return_value.__enter__.return_value.cursor.return_value = (
                mock_cursor
            )

            delete_student(123)

            mock_cursor.execute.assert_called()


if __name__ == "__main__":
    unittest.main()
