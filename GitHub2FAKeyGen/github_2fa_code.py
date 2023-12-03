import pyotp
import pyperclip  # Import the pyperclip library
import subprocess

# Get the TOTP secret key from GitHub (Replace with your own key)
secret_key = "REPLACEYOURKEY"  # Replace with your own QR code data

# Generate a 2FA code using PyOTP
totp = pyotp.TOTP(secret_key)
two_factor_code = totp.now()
print("2FA Code:", two_factor_code)

# Copy the 2FA code to the clipboard
pyperclip.copy(two_factor_code)
print("2FA Code copied to clipboard.")

# Automatically close the console
subprocess.run(["taskkill", "/F", "/IM", "cmd.exe"])
