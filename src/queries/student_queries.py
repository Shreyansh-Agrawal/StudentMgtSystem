class StudentQueries:
    CREATE_TABLE = '''
        CREATE TABLE IF NOT EXISTS students (
            roll_no INTEGER PRIMARY KEY, 
            name TEXT, 
            age INTEGER, 
            gender TEXT, 
            phone TEXT, 
            date_of_joining TEXT, 
            date_of_entry TEXT
        )'''
    ADD_STUDENT = 'INSERT INTO students VALUES (?, ?, ?, ?, ?, ?, ?)'
    GET_STUDENT = 'SELECT * FROM students WHERE roll_no = ?'
    GET_ALL_STUDENTS = 'SELECT * FROM students ORDER BY roll_no'
    UPDATE_STUDENT = 'UPDATE students SET name = ? WHERE roll_no = ?'
    DELETE_STUDENT = 'DELETE FROM students WHERE roll_no = ?'
