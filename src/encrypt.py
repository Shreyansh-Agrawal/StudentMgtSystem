from cryptography.fernet import Fernet

"""executed once to generate key"""

# key = Fernet.generate_key()

# with open('filekey.key', 'wb') as filekey:
#    filekey.write(key)


# Gets the key stored in .key file
def get_key():
    with open("filekey.key", "rb") as file:
        key = file.read()
        return key


# Encrypts the password
def encrypt_password(password):
    password = bytes(password, "utf-8")
    fernet = Fernet(get_key())
    cipher = fernet.encrypt(password)
    return cipher


# Decrypts the password
def decrypt_password(encrypted_password):
    fernet = Fernet(get_key())
    plain_text = fernet.decrypt(encrypted_password)
    return plain_text


# password = '123456'
# cipher = encrypt_password(password)
# # print(cipher)

# plain_text = decrypt_password(cipher)
# print(plain_text)
