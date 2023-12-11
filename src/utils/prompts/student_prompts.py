from controllers import student_controller
from utils.validations import student_validation
from tabulate import tabulate
from datetime import datetime, timezone


def prompt_add_student():
    name = student_validation.validate_name().title()
    roll_no = student_validation.validate_roll_no()
    age = student_validation.validate_age()
    gender = student_validation.validate_gender()
    phone = student_validation.validate_phone()
    date_of_joining = student_validation.validate_date_of_joining()

    time = datetime.now(timezone.utc)  # current utc time
    date_of_entry = time.strftime("%Y-%m-%d")  # yyyy-mm-dd

    try:
        roll_no = int(roll_no)
        age = int(age)

        student_controller.add_student(
            roll_no, name, age, gender, phone, date_of_joining, date_of_entry
        )
    except ValueError:
        print("\nRoll number and Age must be a number!")
    except:
        print("\nAn error occured!")


def prompt_search_student():
    roll_no = student_validation.validate_roll_no()

    try:
        roll_no = int(roll_no)

        student = student_controller.get_student(roll_no)

        if not student:
            print("\nNo such student added!")
            return

        print(
            tabulate(
                student,
                headers={
                    "roll_no": "Roll No.",
                    "name": "Name",
                    "age": "Age",
                    "gender": "Gender",
                    "phone": "Phone",
                    "date_of_joining": "Date of Joining",
                    "date_of_entry": "Date of Entry",
                },
                tablefmt="rounded_outline",
            )
        )
    except ValueError:
        print("\nRoll number must be a number!")
    except:
        print("\nAn error occured!")


def search_all_students():
    students = student_controller.get_all_students()

    if not students:
        print("\nNo students added!")
        return

    print(
        tabulate(
            students,
            headers={
                "roll_no": "Roll No.",
                "name": "Name",
                "age": "Age",
                "gender": "Gender",
                "phone": "Phone",
                "date_of_joining": "Date of Joining",
                "date_of_entry": "Date of Entry",
            },
            tablefmt="rounded_outline",
        )
    )


def prompt_update_student():
    roll_no = student_validation.validate_roll_no()

    try:
        roll_no = int(roll_no)
        student = student_controller.get_student(roll_no)

        if not student:
            print("\nNo such student!")
            return

        new_name = input("Enter the updated name: ").title()

        student_controller.update_student(roll_no, new_name)
    except ValueError:
        print("\nRoll number must be a number!")
    except:
        print("\nAn error occured!")


def prompt_delete_student():
    roll_no = student_validation.validate_roll_no()

    try:
        roll_no = int(roll_no)
        student = student_controller.get_student(roll_no)

        if not student:
            print("\nNo such student!")
            return

        student_controller.delete_student(roll_no)
    except ValueError:
        print("\nRoll number must be a number!")
    except:
        print("\nAn error occured!")
