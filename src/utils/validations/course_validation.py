import re

def error_handling(func):
    def wrapper(*args, **kwargs):
        try:
            res = func(*args, **kwargs)
            if res == False:
                raise Exception
        except:
            print("Please try again...\n")
        finally:
            return res
        
    return wrapper


@error_handling
def validator(pattern, input_data):
    x = re.fullmatch(pattern, input_data)
    if x == None:
        print("Invalid Input Format!")
        return False
    return True

# todo: improve regex
def validate_course_name():
    result = False
    course_name = ''

    while not result:
        course_name = input("Enter Course Name: ").title()
        result = validator('[a-zA-Z ]{5,}', course_name)

    return course_name

# todo: improve regex
def validate_course_id():
    result = False
    course_id = ''

    while not result:
        course_id = input("Enter Course ID: ").upper()
        result = validator('[A-Z0-9]{7}', course_id)
    
    return course_id

# todo: improve regex
def validate_course_credits():
    result = False
    credits = 0

    while not result:
        credits = input("Enter Course Credits: ")
        result = validator('[1-5]', credits)

    return credits

# todo: improve regex
def validate_course_discipline():
    result = False
    discipline = ''

    while not result:
        discipline = input("Enter Course Discipline: ").title()
        result = validator('[A-Za-z ]{2,25}', discipline)
    
    return discipline


if __name__ == '__main__':
    pass
