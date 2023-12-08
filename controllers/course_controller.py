import sqlite3
from utils.database_connection import DatabaseConnection
from typing import List, Dict, Union
from queries.course_queries import CourseQueries
from queries.registration_queries import RegistrationQueries

# Course datatype
Course = Dict[str, Union[str, int]]

def create_course_table() -> None:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute(CourseQueries.CREATE_TABLE)


def add_course(course_id: str, course_name: str, course_credits: int, course_discipline: str, date_of_entry: str) -> None:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        try:
            cursor.execute(CourseQueries.ADD_COURSE, (course_id, course_name, course_credits, course_discipline, date_of_entry))
            print(f"\nCourse: {course_name}, Course ID: {course_id} added!")
        except sqlite3.IntegrityError:
            print("\nCourse ID already exists!")
        except:
            print("\nAn error occured while adding the course!")


def get_course(course_id: str) -> List[Course]:
    course = []

    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        try:
            cursor.execute(CourseQueries.GET_COURSE, (course_id,))
            course = [{'course_id': row[0], 'course_name': row[1], 'course_credits': row[2], 'course_discipline': row[3], 'date_of_entry': row[4]} for row in cursor.fetchall()]
        except:
            print("Some error occured!")

    return course


def get_all_courses() -> List[Course]:
    courses = []

    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        try:
            cursor.execute(CourseQueries.GET_ALL_COURSES)
            courses = [{'course_id': row[0], 'course_name': row[1], 'course_credits': row[2], 'course_discipline': row[3], 'date_of_entry': row[4]} for row in cursor.fetchall()]
        except:
            print("Some error occured!")

    return courses


def update_course(course_id: str, new_course_name: str) -> None:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        try:
            cursor.execute(RegistrationQueries.ENABLE_FOREIGN_KEYS)
            cursor.execute(CourseQueries.UPDATE_COURSE, (new_course_name, course_id))
            print(f"\nCourse id: {course_id} updated as {new_course_name}")
        except sqlite3.IntegrityError:
            print("\nWrong data type")
        except:
            print("\nAn error occured while updating the course!")


def delete_course(course_id: str) -> None:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        try:
            cursor.execute(RegistrationQueries.ENABLE_FOREIGN_KEYS)
            cursor.execute(CourseQueries.DELETE_COURSE, (course_id,))
            print(f"\nCourse with course id: {course_id} deleted!")
        except sqlite3.IntegrityError:
            print("\nWrong data type")
        except:
            print("\nAn error occured while deleting the course!")
