import sqlite3

from src.encrypt import decrypt_password, encrypt_password
from src.utils.custom_error import LoginError
from src.utils.database_connection import DatabaseConnection


def register(user_data):
    username = user_data.get('username')
    password = user_data.get('password')
    role = 'student'

    password = encrypt_password(password)
    with DatabaseConnection("data.db") as connection:
        cursor = connection.cursor()
        try:
            cursor.execute("INSERT INTO users VALUES (?, ?, ?)", (username, password, role))
        except sqlite3.IntegrityError as e:
            raise sqlite3.IntegrityError from e

def login(user_data):
    username = user_data.get('username')
    password = user_data.get('password')
    role = user_data.get('role')
    with DatabaseConnection("data.db") as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT password, role from users WHERE username=?", (username,))
        credentials = cursor.fetchall()
    try:
        db_pswd, db_role = credentials[0]
        decrypted_password = decrypt_password(db_pswd)
        if db_role != role:
            return False
        elif decrypted_password.decode() != password:
            return False
        else:
            return role, username
    except IndexError:
        return False
