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


def validate_name():
    result = False
    name = ''

    while not result:
        name = input("Enter Student name: ").title()
        result = validator('[A-Za-z ]{2,25}', name)

    return name


def validate_roll_no():
    result = False
    roll_no = ''

    while not result:
        roll_no = input("Enter Student Roll No: ")
        result = validator('[1-9][0-9]?', roll_no)
    
    return roll_no


def validate_age():
    result = False
    age = 0

    while not result:
        age = input("Enter Student Age: ")
        result = validator('[1-9][0-9]?', age)

    return age


def validate_gender():
    result = False
    gender = ''

    while not result:
        gender = input("Enter Student Gender (M/F): ").upper()
        result = validator('[M|F]', gender)
    
    return gender


def validate_phone():
    result = False
    phone = ''

    while not result:
        phone = input("Enter Student Phone No: ")
        result = validator('^[1-9][0-9]{9}', phone)
    
    return phone


def validate_date_of_joining():
    result = False
    date_of_joining = ''

    while not result:
        date_of_joining = input("Enter the Date of Joining (yyyy-mm-dd): ")
        result = validator('20[0-2][0-9]-[0-9]{2}-[0-9]{2}', date_of_joining)
    
    return date_of_joining


if __name__ == '__main__':
    validate_roll_no()
