import time

# A function to calculate the estimated time to crack a password
def calculate_password_crack_time(password):
    # Define the character set used to create the password
    character_set = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_-+={}[]|\:;\"'<>,.?/"
    # Determine the length of the password
    password_length = len(password)
    # Calculate the total number of possible combinations
    possibilities = len(character_set) ** password_length
    # Set the number of guesses that can be made per second
    guesses_per_second = 10 ** 9
    # Calculate the estimated time to crack the password in seconds, minutes, hours, days, and years
    seconds = possibilities / guesses_per_second
    minutes = seconds / 60
    hours = minutes / 60
    days = hours / 24
    years = days / 365

    # Print the password length, total number of combinations, and estimated number of guesses
    print("Estimated password length: {}".format(password_length))
    print("Estimated number of combinations: {:,}".format(possibilities))
    print("Estimated number of guesses (1 billion/s): {:,}".format(int(possibilities/guesses_per_second)))
    print("Estimated crack time:")
    # Print the estimated time to crack the password in years, days, hours, minutes, or seconds
    if years > 1:
        print("{:.0f} years".format(years))
    elif days > 1:
        print("{:.0f} days".format(days))
    elif hours > 1:
        print("{:.0f} hours".format(hours))
    elif minutes > 1:
        print("{:.0f} minutes".format(minutes))
    else:
        print("{:.0f} seconds".format(seconds))

# Main function
if __name__ == "__main__":
    # Prompt user to enter their password
    password = input("Enter your password: ")
    # Record the start time
    start = time.time()
    # Calculate the estimated time to crack the password
    calculate_password_crack_time(password)
    # Record the end time
    end = time.time()
    # Print the total execution time of the program
    print("Program execution time: {:.2f} seconds".format(end-start))
