import sqlite3
import unittest
from unittest.mock import MagicMock, patch

from controllers.course_controller import (add_course, create_course_table,
                                           delete_course, get_all_courses,
                                           get_course, update_course)


class TestCourseFunctions(unittest.TestCase):
    def test_create_course_table(self):
        with patch("controllers.course_controller.DatabaseConnection") as mock_db_connection:
            mock_cursor = MagicMock()
            mock_db_connection.return_value.__enter__.return_value.cursor.return_value = (
                mock_cursor
            )
            create_course_table()
            mock_cursor.execute.assert_called_once()

    def test_add_course(self):
        with patch("controllers.course_controller.DatabaseConnection") as mock_db_connection:
            mock_cursor = MagicMock()
            mock_db_connection.return_value.__enter__.return_value.cursor.return_value = (
                mock_cursor
            )
            add_course("CS101", "Computer Science", 3, "Computer Science", "2023-01-01")
            mock_cursor.execute.assert_called_once()

    def test_add_course_err(self):
        with patch("controllers.course_controller.DatabaseConnection") as mock_db_connection:
            mock_cursor = MagicMock()
            mock_db_connection.return_value.__enter__.return_value.cursor.return_value = (
                mock_cursor
            )
            mock_cursor.execute.side_effect = sqlite3.IntegrityError
            add_course("CS101", "Computer Science", 3, "Computer Science", "2023-01-01")
            mock_cursor.execute.assert_called_once()

    def test_add_course_exp(self):
        with patch("controllers.course_controller.DatabaseConnection") as mock_db_connection:
            mock_cursor = MagicMock()
            mock_db_connection.return_value.__enter__.return_value.cursor.return_value = (
                mock_cursor
            )
            mock_cursor.execute.side_effect = Exception
            add_course("CS101", "Computer Science", 3, "Computer Science", "2023-01-01")
            mock_cursor.execute.assert_called_once()

    def test_get_course(self):
        with patch("controllers.course_controller.DatabaseConnection") as mock_db_connection:
            mock_cursor = MagicMock()
            mock_cursor.fetchall.return_value = [
                ("CS101", "Computer Science", 3, "Computer Science", "2023-01-01")
            ]
            mock_db_connection.return_value.__enter__.return_value.cursor.return_value = (
                mock_cursor
            )
            course = get_course("CS101")
            self.assertEqual(len(course), 1)
            self.assertEqual(course[0]["course_name"], "Computer Science")

    def test_get_all_courses(self):
        with patch(
            "controllers.course_controller.DatabaseConnection"
        ) as mock_db_connection:
            mock_cursor = MagicMock()
            mock_cursor.fetchall.return_value = [
                ("CS101", "Computer Science", 3, "Computer Science", "2023-01-01"),
                ("ENG101", "English", 3, "Language", "2023-01-01"),
            ]
            mock_db_connection.return_value.__enter__.return_value.cursor.return_value = (
                mock_cursor
            )
            courses = get_all_courses()
            self.assertEqual(len(courses), 2)
            self.assertEqual(courses[0]["course_name"], "Computer Science")
            self.assertEqual(courses[1]["course_discipline"], "Language")

    def test_update_course(self):
        with patch(
            "controllers.course_controller.DatabaseConnection"
        ) as mock_db_connection:
            mock_cursor = MagicMock()
            mock_db_connection.return_value.__enter__.return_value.cursor.return_value = (
                mock_cursor
            )
            update_course("CS101", "New Computer Science")
            assert mock_cursor.execute.call_count == 2

    def test_update_course_err(self):
        with patch(
            "controllers.course_controller.DatabaseConnection"
        ) as mock_db_connection:
            mock_cursor = MagicMock()
            mock_db_connection.return_value.__enter__.return_value.cursor.return_value = (
                mock_cursor
            )
            mock_cursor.execute.side_effect = sqlite3.IntegrityError
            update_course("CS101", "New Computer Science")
            assert mock_cursor.execute.call_count == 1

    def test_update_course_exp(self):
        with patch(
            "controllers.course_controller.DatabaseConnection"
        ) as mock_db_connection:
            mock_cursor = MagicMock()
            mock_db_connection.return_value.__enter__.return_value.cursor.return_value = (
                mock_cursor
            )
            mock_cursor.execute.side_effect = Exception
            update_course("CS101", "New Computer Science")
            assert mock_cursor.execute.call_count == 1

    def test_delete_course(self):
        with patch(
            "controllers.course_controller.DatabaseConnection"
        ) as mock_db_connection:
            mock_cursor = MagicMock()
            mock_db_connection.return_value.__enter__.return_value.cursor.return_value = (
                mock_cursor
            )
            delete_course("CS101")
            assert mock_cursor.execute.call_count == 2

    def test_delete_course_err(self):
        with patch(
            "controllers.course_controller.DatabaseConnection"
        ) as mock_db_connection:
            mock_cursor = MagicMock()
            mock_db_connection.return_value.__enter__.return_value.cursor.return_value = (
                mock_cursor
            )
            mock_cursor.execute.side_effect = sqlite3.IntegrityError
            delete_course("CS101")
            assert mock_cursor.execute.call_count == 1

    def test_delete_course_exp(self):
        with patch(
            "controllers.course_controller.DatabaseConnection"
        ) as mock_db_connection:
            mock_cursor = MagicMock()
            mock_db_connection.return_value.__enter__.return_value.cursor.return_value = (
                mock_cursor
            )
            mock_cursor.execute.side_effect = Exception
            delete_course("CS101")
            assert mock_cursor.execute.call_count == 1


if __name__ == "__main__":
    unittest.main()
