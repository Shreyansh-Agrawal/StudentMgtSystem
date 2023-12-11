from utils.prompts import course_prompts
from utils.prompts import student_prompts
from utils.prompts import registration_prompts

STUDENT_CHOICE = """
Enter -
        1 - To add a Student
        2 - Search a Student with Roll Number
        3 - View all Students
        4 - Update Student Details
        5 - Delete a Student
        
        Press q to quit

Enter your choice: """

COURSE_CHOICE = """
Enter -
        1 - To add a Course
        2 - Search a Course with Course ID
        3 - View all Courses
        4 - Update Course Details
        5 - Delete a Course
        
        Press q to Quit

Enter your choice: """

REGISTRATION_CHOICE = """
Enter -
        1 - To Enroll a Student into a Course
        2 - Search Registrations for a Student
        3 - View all Registrations
        4 - Update Registration Details
        5 - Delete a Registration
        
        Press q to Quit

Enter your choice: """


def student_menu():
    user_input = input(STUDENT_CHOICE)

    while user_input != "q":
        match user_input:
            case "1":
                student_prompts.prompt_add_student()
            case "2":
                student_prompts.prompt_search_student()
            case "3":
                student_prompts.search_all_students()
            case "4":
                student_prompts.prompt_update_student()
            case "5":
                student_prompts.prompt_delete_student()
            case _:
                print("Wrong input! Please choose from the above given inputs...")

        user_input = input(STUDENT_CHOICE)


def course_menu():
    user_input = input(COURSE_CHOICE)

    while user_input != "q":
        match user_input:
            case "1":
                course_prompts.prompt_add_course()
            case "2":
                course_prompts.prompt_search_course()
            case "3":
                course_prompts.search_all_courses()
            case "4":
                course_prompts.prompt_update_course()
            case "5":
                course_prompts.prompt_delete_course()
            case _:
                print("Wrong input! Please choose from the above given inputs...")

        user_input = input(COURSE_CHOICE)


def registration_menu():
    user_input = input(REGISTRATION_CHOICE)

    while user_input != "q":
        match user_input:
            case "1":
                registration_prompts.prompt_add_registration()
            case "2":
                registration_prompts.prompt_search_registration()
            case "3":
                registration_prompts.search_all_registrations()
            case "4":
                registration_prompts.prompt_update_registration()
            case "5":
                registration_prompts.prompt_delete_registration()
            case _:
                print("Wrong input! Please choose from the above given inputs...")

        user_input = input(REGISTRATION_CHOICE)
