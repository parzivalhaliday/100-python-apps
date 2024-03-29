# GitHub2FAKeyGen

GitHub2FAKeyGen is a Python application that automatically generates two-factor authentication (2FA) codes for GitHub. This tool provides you with a quick authentication code when 2FA is required for accessing your GitHub account.


![github2fa](https://github.com/parzivalhaliday/100-python-apps/blob/main/GitHub2FAKeyGen/GitHub2FAKeyGen.png)


## How to Use

1. Run the application: `python github2fakeygen.py`
2. In the first step, you will need to enter your username and password.
3. Next, you will be prompted to enter the key (secret_key) obtained from the 2FA QR code of your GitHub account. You can obtain this key by scanning the QR code or from your GitHub account settings.
4. The application will generate a fresh 2FA code every time it is run and automatically copies it to your clipboard.
5. Use the code when logging in to your GitHub account.

## Requirements

- Python
- `pyotp` and `selenium` libraries (you can install them using the `pip install pyotp selenium` command)

## License

You can use the code however you want.
