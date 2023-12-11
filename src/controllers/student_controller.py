import sqlite3
from utils.database_connection import DatabaseConnection
from typing import List, Dict, Union
from queries.student_queries import StudentQueries
from queries.registration_queries import RegistrationQueries

# Student datatype
Student = Dict[str, Union[str, int]]


def create_students_table() -> None:
    with DatabaseConnection("data.db") as connection:
        cursor = connection.cursor()

        cursor.execute(StudentQueries.CREATE_TABLE)


def add_student(
    roll_no: int,
    name: str,
    age: int,
    gender: str,
    phone: str,
    date_of_joining: str,
    date_of_entry: str,
) -> None:
    with DatabaseConnection("data.db") as connection:
        cursor = connection.cursor()
        try:
            cursor.execute(
                StudentQueries.ADD_STUDENT,
                (roll_no, name, age, gender, phone, date_of_joining, date_of_entry),
            )
            print(f"\nStudent: {name}, Roll No: {roll_no} added!")
        except sqlite3.IntegrityError:
            print("\nRoll number already exists!")
        except Exception as e:
            print(f"\nAn error occured while adding the student!\n{e}")


def get_student(roll_no: int) -> List[Student]:
    student = []

    with DatabaseConnection("data.db") as connection:
        cursor = connection.cursor()
        try:
            cursor.execute(StudentQueries.GET_STUDENT, (roll_no,))
            student = [
                {
                    "roll_no": row[0],
                    "name": row[1],
                    "age": row[2],
                    "gender": row[3],
                    "phone": row[4],
                    "date_of_joining": row[5],
                    "date_of_entry": row[6],
                }
                for row in cursor.fetchall()
            ]
        except:
            print("Some error occured!")

    return student


def get_all_students() -> List[Student]:
    students = []

    with DatabaseConnection("data.db") as connection:
        cursor = connection.cursor()
        try:
            cursor.execute(StudentQueries.GET_ALL_STUDENTS)
            students = [
                {
                    "roll_no": row[0],
                    "name": row[1],
                    "age": row[2],
                    "gender": row[3],
                    "phone": row[4],
                    "date_of_joining": row[5],
                    "date_of_entry": row[6],
                }
                for row in cursor.fetchall()
            ]
        except:
            print("Some error occured!")

    return students


def update_student(roll_no: int, new_name: str) -> None:
    with DatabaseConnection("data.db") as connection:
        cursor = connection.cursor()
        try:
            cursor.execute(RegistrationQueries.ENABLE_FOREIGN_KEYS)
            cursor.execute(StudentQueries.UPDATE_STUDENT, (new_name, roll_no))
            print(f"\nRoll no: {roll_no} updated as {new_name}")
        except sqlite3.IntegrityError:
            print("\nWrong data type")
        except Exception as e:
            print(f"\nAn error occured while updating the student!\n{e}")


def delete_student(roll_no: int) -> None:
    with DatabaseConnection("data.db") as connection:
        cursor = connection.cursor()
        try:
            cursor.execute(RegistrationQueries.ENABLE_FOREIGN_KEYS)
            cursor.execute(StudentQueries.DELETE_STUDENT, (roll_no,))
            print(f"\nStudent with roll no: {roll_no} deleted!")
        except sqlite3.IntegrityError:
            print("\nWrong data type")
        except Exception as e:
            print(f"\nAn error occured while deleting the student!\n{e}")
