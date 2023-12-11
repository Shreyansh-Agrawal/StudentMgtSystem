import sqlite3

from utils.database_connection import DatabaseConnection
from typing import List, Dict, Union
from queries.registration_queries import RegistrationQueries

# Registration datatype
Registration = Dict[str, Union[str, int]]


def create_registration_table() -> None:
    with DatabaseConnection("data.db") as connection:
        cursor = connection.cursor()

        cursor.execute(RegistrationQueries.ENABLE_FOREIGN_KEYS)
        cursor.execute(RegistrationQueries.CREATE_TABLE)


def add_registration(roll_no: int, course_id: str, date_of_entry: str) -> None:
    with DatabaseConnection("data.db") as connection:
        cursor = connection.cursor()
        try:
            cursor.execute(RegistrationQueries.ENABLE_FOREIGN_KEYS)
            cursor.execute(
                RegistrationQueries.ADD_REGISTRATION,
                (roll_no, course_id, date_of_entry),
            )
            print(f"\nRoll no: {roll_no} Enrolled in Course: {course_id} successfully!")
        except sqlite3.IntegrityError as e:
            print(
                f"\nAn error occured: IntegrityError [add_registration, registration_controller.py]\n{e}"
            )
        except sqlite3.OperationalError as e:
            print(
                f"\nAn error occured: OperationalError [add_registration, registration_controller.py]\n{e}"
            )


def get_registration(roll_no: int) -> List[Registration]:
    registration = []

    with DatabaseConnection("data.db") as connection:
        cursor = connection.cursor()
        try:
            cursor.execute(RegistrationQueries.GET_REGISTRATION, (roll_no,))
            registration = [
                {"roll_no": row[0], "course_id": row[1], "date_of_entry": row[2]}
                for row in cursor.fetchall()
            ]
        except:
            print("\nAn error occured [get_registration, registration_controller.py]")

    return registration


def get_all_registrations() -> List[Registration]:
    registrations = []

    with DatabaseConnection("data.db") as connection:
        cursor = connection.cursor()
        try:
            cursor.execute(RegistrationQueries.GET_ALL_REGISTRATIONS)
            registrations = [
                {
                    "roll_no": row[0],
                    "name": row[1],
                    "course_id": row[2],
                    "course_name": row[3],
                    "date_of_registration": row[4],
                }
                for row in cursor.fetchall()
            ]
        except Exception as e:
            print(
                f"\nAn error occured [get_all_registrations, registration_controller.py]\n{e}"
            )

    return registrations


def update_registration(roll_no: int, course_id: str, new_course_id: str) -> None:
    with DatabaseConnection("data.db") as connection:
        cursor = connection.cursor()
        try:
            cursor.execute(
                RegistrationQueries.UPDATE_REGISTRATION,
                (new_course_id, roll_no, course_id),
            )
            print(
                f"Updated Course: {new_course_id} from {course_id} for Roll No: {roll_no}"
            )
        except sqlite3.IntegrityError as e:
            print(
                f"\nAn error occured: IntegrityError [update_registration, registration_controller.py]\n{e}"
            )
        except sqlite3.OperationalError as e:
            print(
                f"\nAn error occured: OperationalError [update_registration, registration_controller.py]\n{e}"
            )


def delete_registration(roll_no: int, course_id: str) -> None:
    with DatabaseConnection("data.db") as connection:
        cursor = connection.cursor()
        try:
            cursor.execute(
                RegistrationQueries.DELETE_REGISTRATION, (roll_no, course_id)
            )
            print(
                f"\nRegistration of Roll No: {roll_no} for course: {course_id} deleted!"
            )
        except sqlite3.IntegrityError as e:
            print(
                f"\nAn error occured: IntegrityError [delete_registration, registration_controller.py]\n{e}"
            )
        except sqlite3.OperationalError as e:
            print(
                f"\nAn error occured: OperationalError [delete_registration, registration_controller.py]\n{e}"
            )
