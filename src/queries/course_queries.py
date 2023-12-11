class CourseQueries:
    CREATE_TABLE = """
        CREATE TABLE IF NOT EXISTS courses (
            course_id TEXT PRIMARY KEY, 
            course_name TEXT, 
            course_credits INTEGER, 
            course_discipline TEXT, 
            date_of_entry TEXT
        )"""
    ADD_COURSE = "INSERT INTO courses VALUES (?, ?, ?, ?, ?)"
    GET_COURSE = "SELECT * FROM courses WHERE course_id = ?"
    GET_ALL_COURSES = "SELECT * FROM courses ORDER BY course_id"
    UPDATE_COURSE = "UPDATE courses SET course_name = ? WHERE course_id = ?"
    DELETE_COURSE = "DELETE FROM courses WHERE course_id = ?"
