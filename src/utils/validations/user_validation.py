import maskpass
import logging
from utils.database_connection import DatabaseConnection
from utils.custom_error import LoginError
from encrypt import encrypt_password, decrypt_password

ATTEMPT_LIMIT = 3
ROLES = ["admin", "student"]

# def temp():
#     # p1 = '123456'
#     # p2 = 'qwerty'
#     # ep1 = encrypt_password(p1)
#     # ep2 = encrypt_password(p2)

#     with DatabaseConnection('data.db') as connection:
#         cursor = connection.cursor()
#         cursor.execute('insert into users values("admin", ?, "admin")', (ep1, ))
#         cursor.execute('insert into users values("student", ?, "student")', (ep2, ))

# temp()

logging.basicConfig(
    format="%(asctime)s %(levelname)-8s %(message)s",
    datefmt="%d-%m-%Y %H:%M:%S",
    level=logging.INFO,
    filename="logs.txt",
)

logger = logging.getLogger(__name__)


def validate_user(role):
    username = input("Enter username: ")
    password = maskpass.askpass(mask="*")

    with DatabaseConnection("data.db") as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT password, role from users WHERE username=?", (username,))
        credentials = cursor.fetchall()
    try:
        db_pswd, db_role = credentials[0]
        decrypted_password = decrypt_password(db_pswd)

        if db_role != role:
            return False
        elif decrypted_password.decode() != password:
            return False
        else:
            logger.info(username)
            print("\nLogged in successfully!")
            return True
    except IndexError:
        print("Wrong credentials!")
        return False
    except Exception as e:
        print(e)
        return False


def input_user_role():
    role = input("Choose role (Admin | Student): ").lower()
    return role


def validate_role():
    attempts_remaining = ATTEMPT_LIMIT

    role = input_user_role()

    while role not in ROLES:
        print("Role does not exists! Please try again...\n")
        role = input_user_role()

    while not validate_user(role):
        print("\nInvalid credentials! Try again...\n")
        attempts_remaining -= 1
        print(f"Remaining attempts: {attempts_remaining}")

        if attempts_remaining == 0:
            raise LoginError("No more attempts allowed!")

    return role
