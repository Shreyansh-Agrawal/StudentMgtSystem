import pytest

from controllers.course_controller import create_course_table
from controllers.registration_controller import create_registration_table
from controllers.student_controller import create_students_table
from queries.course_queries import CourseQueries
from queries.registration_queries import RegistrationQueries
from queries.student_queries import StudentQueries
from utils.database_connection import DatabaseConnection
from utils.prompts.file_paths import FilePaths


@pytest.fixture(autouse=True, scope='package')
def handle_db(package_mocker):
    package_mocker.patch.object(FilePaths, 'DB_PATH', FilePaths.TEST_PATH)
    create_course_table()
    create_students_table()
    create_registration_table()


@pytest.fixture(autouse=True, scope='package')
def insert_test_data():
    with DatabaseConnection("test.db") as connection:
        cursor = connection.cursor()
        cursor.execute(CourseQueries.ADD_COURSE, ("CSE101", "Computer Science", 3, "Computer Science", "2023-01-01"))
        cursor.execute(RegistrationQueries.ADD_REGISTRATION, (123, 'CS101', '2023-01-01'))
        cursor.execute(StudentQueries.ADD_STUDENT, (123, "John Doe", 20, "Male", "1234567890", "2023-01-01", "2023-01-01"))

    yield
    
    with DatabaseConnection("test.db") as connection:
        cursor = connection.cursor()
        cursor.execute('DROP TABLE courses')
        cursor.execute('DROP TABLE registration')
        cursor.execute('DROP TABLE students')
        