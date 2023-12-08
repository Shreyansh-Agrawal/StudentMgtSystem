class RegistrationQueries:
    CREATE_TABLE = '''CREATE TABLE IF NOT EXISTS registration (
        roll_no INTEGER, 
        course_id TEXT, 
        date_of_registration TEXT,
        FOREIGN KEY(roll_no) REFERENCES students(roll_no) ON DELETE CASCADE, 
        FOREIGN KEY(course_id) REFERENCES courses(course_id) ON DELETE CASCADE, 
        PRIMARY KEY(roll_no, course_id)
    )'''
    ADD_REGISTRATION = 'INSERT INTO registration VALUES(?, ?, ?)'
    GET_REGISTRATION = 'SELECT * FROM registration WHERE roll_no = ?'
    GET_ALL_REGISTRATIONS = '''SELECT 
        registration.roll_no, students.name, registration.course_id, courses.course_name, registration.date_of_registration FROM 
        students INNER JOIN registration INNER JOIN courses 
        WHERE students.roll_no = registration.roll_no AND courses.course_id = registration.course_id 
        ORDER BY registration.roll_no'''
    UPDATE_REGISTRATION = 'UPDATE registration set course_id = ? where roll_no = ? and course_id = ?'
    DELETE_REGISTRATION = 'DELETE FROM registration WHERE roll_no = ? and course_id = ?'
    ENABLE_FOREIGN_KEYS = "PRAGMA foreign_keys = 1"
