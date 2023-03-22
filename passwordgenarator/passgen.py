import random
import string
import re
import hashlib

# Function for hashing the password
def hash_password(password):
    salt = 'random_salt'
    hashed_password = hashlib.sha256((password + salt).encode()).hexdigest()
    return hashed_password

# List of possible characters
letters = string.ascii_letters
digits = string.digits
punctuations = string.punctuation

# Get the minimum password length from the user
while True:
    try:
        length = int(input('What minimum length would you like your password to be? '))
        if length < 16:
            print('Please choose a password length of at least 16 characters.')
        else:
            break
    except ValueError:
        print('Please enter a number.')

# Function for generating a password
def generate_password():
    while True:
        # Password length must be at least the specified minimum length
        password = random.choice(letters) + ''.join(random.choice(letters + digits + punctuations) for i in range(length - 1))

        # Must contain at least 2 digits, 2 uppercase letters, and 3 special characters
        if not re.search(r'\d{2,}', password):
            continue
        if not re.search(r'[A-Z]{2,}', password):
            continue
        if not re.search(r'[!@#$%^&*()_+-=]{3,}', password):
            continue

        return password

# Generate a new password
password = generate_password()

# Hash the password
hashed_password = hash_password(password)

# Write the hashed password to a file
with open('passwords.txt', 'a') as file:
    file.write(hashed_password + '\n')

# Print the generated password and the hashed password
print('Generated password:', password)
print('Hashed password:', hashed_password)
