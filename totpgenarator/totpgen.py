import pyotp
import pyperclip

# Get the shared secret from the user
shared_secret = input("Enter the Shared Secret: ")

# Create a TOTP (Time-based One-Time Password) object
totp = pyotp.TOTP(shared_secret)

# Generate a one-time password
otp = totp.now()

# Display the generated one-time password to the user
print(f"One-Time Password: {otp}")

# Copy the password to the clipboard
pyperclip.copy(otp)

print("Password Copied to Clipboard.")
