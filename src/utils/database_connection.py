"""This is a context manager for database connection to sqlite"""
import sqlite3

from utils.prompts.file_paths import FilePaths


class DatabaseConnection:
    """A class for database context manager"""

    def __init__(self, host):
        self.connection = None
        self.host = FilePaths.DB_PATH

    def __enter__(self):
        self.connection = sqlite3.connect(self.host)
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type or exc_val or exc_tb:
            self.connection.close()
        else:
            self.connection.commit()
            self.connection.close()


# class DatabaseManager:
#     _instance = None

#     def __new__(cls, db_file='data.db'):
#         if cls._instance is None:
#             cls._instance = super(DatabaseManager, cls).__new__(cls)
#             cls._instance.connection = sqlite3.connect(db_file)
#         return cls._instance

#     def __enter__(self):
#         return self.connection

#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.connection.close()
