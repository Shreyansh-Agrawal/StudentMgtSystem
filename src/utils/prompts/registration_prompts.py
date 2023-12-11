from utils.prompts.course_prompts import search_all_courses
from controllers import registration_controller, course_controller, student_controller
from utils.validations import course_validation, student_validation
from tabulate import tabulate
from datetime import datetime, timezone


def prompt_add_registration():
    # lists out all courses
    print("\nChoose from the list of courses given below-")
    search_all_courses()
    roll_no = student_validation.validate_roll_no()
    course_id = course_validation.validate_course_id()

    time = datetime.now(timezone.utc)  # current utc time
    date_of_entry = time.strftime("%Y-%m-%d")  # yyyy-mm-dd

    try:
        roll_no = int(roll_no)

        registration_controller.add_registration(roll_no, course_id, date_of_entry)
    except ValueError:
        print("\nRoll number must be a number!")
    except Exception as e:
        print(f"\nAn error occured!\n{e}")


def prompt_search_registration():
    roll_no = student_validation.validate_roll_no()

    try:
        roll_no = int(roll_no)

        registration = registration_controller.get_registration(roll_no)

        if not registration:
            print(f"\nNo registration found for Roll No. {roll_no}")
            return

        print(
            tabulate(
                registration,
                headers={"roll_no": "Roll No.", "course_id": "Course ID"},
                tablefmt="rounded_outline",
            )
        )
    except ValueError:
        print("\nRoll number must be a number!")
    except Exception as e:
        print(f"\nAn error occured!\n{e}")


def search_all_registrations():
    registrations = registration_controller.get_all_registrations()

    if not registrations:
        print("\nNo registrations found!")
        return

    print(
        tabulate(
            registrations,
            headers={
                "roll_no": "Roll No.",
                "name": "Name",
                "course_id": "Course ID",
                "course_name": "Course",
                "date_of_registration": "Date of Registration",
            },
            tablefmt="rounded_outline",
        )
    )


def prompt_update_registration():
    try:
        roll_no = student_validation.validate_roll_no()
        roll_no = int(roll_no)
        student = student_controller.get_student(roll_no)

        if not student:
            print("\nNo such student!")
            return

        course_id = course_validation.validate_course_id()
        course = course_controller.get_course(course_id)

        if not course:
            print("\nNo such course!")
            return

        new_course_id = input("Enter Updated Course ID: ").upper()
        new_course = course_controller.get_course(new_course_id)

        if not new_course:
            print("\nNo such course!")
            return

        registration_controller.update_registration(roll_no, course_id, new_course_id)
    except ValueError:
        print("\nRoll number must be a number!")
    except Exception as e:
        print(f"\nAn error occured!\n{e}")


def prompt_delete_registration():
    try:
        roll_no = student_validation.validate_roll_no()
        roll_no = int(roll_no)
        student = student_controller.get_student(roll_no)

        if not student:
            print("\nNo such student!")
            return

        course_id = course_validation.validate_course_id()
        course = course_controller.get_course(course_id)

        if not course:
            print("\nNo such course!")
            return

        registration_controller.delete_registration(roll_no, course_id)
    except ValueError:
        print("\nRoll number must be a number!")
    except Exception as e:
        print(f"\nAn error occured!\n{e}")
