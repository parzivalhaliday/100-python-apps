import os
from cryptography.fernet import Fernet

def generate_key(filename):
    """Generates a random encryption key for Fernet and saves it to file."""
    key = Fernet.generate_key()
    key_filename = os.path.splitext(filename)[0] + ".key"
    with open(key_filename, "wb") as key_file:
        key_file.write(key)

def load_key(filename):
    """Loads the encryption key from file."""
    key_filename = os.path.splitext(filename)[0] + ".key"
    return open(key_filename, "rb").read()

def encrypt(filename, key):
    """Encrypts the specified file."""
    f = Fernet(key)

    with open(filename, "rb") as file:
        file_data = file.read()

    encrypted_data = f.encrypt(file_data)

    with open(filename, "wb") as file:
        file.write(encrypted_data)

    generate_key(filename)

def decrypt(filename, key):
    """Decrypts the specified file."""
    f = Fernet(key)

    with open(filename, "rb") as file:
        encrypted_data = file.read()

    decrypted_data = f.decrypt(encrypted_data)

    with open(filename, "wb") as file:
        file.write(decrypted_data)

if __name__ == "__main__":
    choice = input("Do you want to generate the encryption key? (y/n): ")
    if choice == "y":
        filename = input("Enter the name of the file to encrypt: ")
        generate_key(filename)

    key = load_key(filename)

    choice = input("Enter 1 to encrypt a file, 2 to decrypt a file: ")

    if choice == "1":
        filename = input("Enter the name of the file to encrypt: ")
        key = load_key(filename)
        encrypt(filename, key)
    elif choice == "2":
        filename = input("Enter the name of the file to decrypt: ")
        key = load_key(filename)
        decrypt(filename, key)
    else:
        print("Invalid choice.")
