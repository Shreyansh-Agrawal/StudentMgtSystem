This project aims to provide functionalities related to student management to schools and colleges 

Modules- 

    1. Student module
        
        Features of Student module:
        - add a student
        - find a student by roll number
        - view all students' details
        - update a student details
        - delete a student
        
    2. Course module
        - crud on courses

    3. Result module
        - view student wise result
        - view all results

```
feedback:

use decorators, explore it
oops concepts other than classes and objects
add validation, use regex
file handling
error handling - first thing to do!
remove brackets from if
use enums, learn about them
learn about match case
take care of sql injection
use UID, explore libraries on it
explore encryption
put a readme for introduction

exception handeling
use match case
study about regex, link in teams

try to implement all the concepts studied till now, even if not needed

- refactor the project structure
- add more functionality
- add more user roles
- create separate file for queries (use const variable naming)
- pylint extension
- reduce code redundancy
```

```
Work done till now -

db connection
used context manager
used type hinting
error handling
kept code modular
taken care of sql injection
used python tabulate library
added login functionality, masked the password, taken care of attempts limit
added regex for validation
used custom error
```

```
Todo - 
    - work on result module
        schema: (s_roll_no, course1_id_marks, course2_id_marks, ...)

        -> when result module is run, it should automatically fill all the roll nos from student table
                - in student module, when a student is added, run insert query on results table to add the roll
                - in student module, when a student is deleted, run delete query on results table to delete the roll
        -> it should automatically take the courses from courses table
                - in course module, when a course is added, run the alter query on results table to add the col
                - in course module when a course is deleted, run the drop query on results table to delete the col
        -> admin should be able to put marks in the cells
                - take user prompts as enter roll no, enter course id and then run insert query on results table to add marks for a cell
                - show the user list of roll nos with names and course id with course names to select from one

        OR

        -> instead of marks, implement assignments
            - each student has some courses, each course has some assignment
            - we can view for a particular student, his courses and assignment status

        -> student enrolls in the courses in comma separated values, from the list of courses shown from courses table
        -> have to add role based auth, handle error
        -> put a check if entered courses are present

            OR

        -> create another table enrollments(roll_no, course_id)
        -> PK - (roll_no, course_id) 
        -> both are FK respectively to student and courses table
        -> need to check if roll_no and course_id exist in their respective tables
                
        earlier -> 
            was modifying the student table, adding another column (courses_enrolled)
            entry was a single string with comma separated values, thought of splitting the string and putting it in list

    - improve courses module
        schema: (course_id, course_name, course_credits)
    - plan for foreign keys, improve logging
    - implement encryption

    - code clean up, modify update student, course functionality,
    - implement encryption in storing password, 
    - use decorator in sql error handling,
    - add more user roles
    - create separate file for queries (use const variable naming)
    - pylint extension
    - reduce code redun
```

```
Work done- 
    - added registration module with foreign key constraints and used joins

todo-
    - refactoring
        - encapsulate funcs to a class
        - use property decorator where possible
        - use pylint
    - registration module 
        - while updating check if the roll no exists in the registration table
        - same while deleting
    - add menu for student role
    - use decorator to check access level
    - use hashlib
    - update role based access, automatically fetch the role
```

Have one database connection, opens when app starts, closes when app closes