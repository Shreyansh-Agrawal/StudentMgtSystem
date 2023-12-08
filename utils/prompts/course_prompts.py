from controllers import course_controller
from utils.validations import course_validation
from tabulate import tabulate
from datetime import datetime, timezone

def prompt_add_course():
    course_name = course_validation.validate_course_name()
    course_id = course_validation.validate_course_id()
    course_credits = course_validation.validate_course_credits()
    course_discipline = course_validation.validate_course_discipline()

    time = datetime.now(timezone.utc) # current utc time
    date_of_entry = time.strftime('%Y-%m-%d') # yyyy-mm-dd

    try:
        course_credits = int(course_credits)

        course_controller.add_course(course_id, course_name, course_credits, course_discipline, date_of_entry)
    except ValueError:
        print("\Course credit must be a number!")
    except:
        print("\nAn error occured!")


def prompt_search_course():
    course_id = course_validation.validate_course_id()

    try:
        course = course_controller.get_course(course_id)

        if not course:
            print("\nNo such course added!")
            return
     
        print(tabulate(course, headers={'course_id': 'Course ID.', 
                                        'course_name': 'Course Name', 
                                        'course_credits': 'Credits', 
                                        'course_discipline': 'Discipline', 
                                        'date_of_entry': 'Date of Entry'
                                        }, 
                                        tablefmt="rounded_outline"))

    except:
        print("\nAn error occured!")


def search_all_courses():
    courses = course_controller.get_all_courses()

    if not courses:
        print("\nNo courses added!")
        return
    
    print(tabulate(courses, headers={'course_id': 'Course ID.', 
                                     'course_name': 'Course Name', 
                                     'course_credits': 'Credits', 
                                     'course_discipline': 'Discipline', 
                                     'date_of_entry': 'Date of Entry'
                                     }, 
                                     tablefmt="rounded_outline"))


def prompt_update_course():
    course_id = course_validation.validate_course_id()

    try:
        course = course_controller.get_course(course_id)
        
        if not course:
            print("\nNo such course!")
            return
        
        new_course_name = input("Enter the updated name: ").title()

        course_controller.update_course(course_id, new_course_name)
    except:
        print("\nAn error occured!")


def prompt_delete_course():
    course_id = course_validation.validate_course_id()

    try:
        course = course_controller.get_course(course_id)
        
        if not course:
            print("\nNo such course!")
            return
        
        course_controller.delete_course(course_id)
    except:
        print("\nAn error occured!")
