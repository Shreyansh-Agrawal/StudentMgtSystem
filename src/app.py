"""This is the entry point of the application"""

from utils.menu import menu_functions
from utils.prompts import course_prompts
from utils.validations import user_validation
from controllers.student_controller import create_students_table
from controllers.course_controller import create_course_table
from controllers.registration_controller import create_registration_table

USER_CHOICE = """
Enter - 
        1 - Go to Students
        2 - Go to Courses
        3 - Go to Registrations

        Press q to quit

Enter your choice: """

create_students_table()
create_course_table()
create_registration_table()


def menu():
    """Menu function"""
    role = user_validation.validate_role()

    if role == "admin":
        user_input = input(USER_CHOICE)

        while user_input != "q":
            match user_input:
                case "1":
                    menu_functions.student_menu()
                case "2":
                    menu_functions.course_menu()
                case "3":
                    menu_functions.registration_menu()
                case _:
                    print("Wrong input! Please choose from the above given options...")

            user_input = input(USER_CHOICE)

    elif role == "student":
        print("You can only view the list of courses offered\n")
        course_prompts.search_all_courses()


if __name__ == "__main__":
    menu()
