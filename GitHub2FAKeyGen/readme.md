# GitHub2FAKeyGen

GitHub2FAKeyGen is a Python application that automatically generates two-factor authentication (2FA) codes for GitHub. This tool provides you with a quick authentication code when 2FA is required for accessing your GitHub account.

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

This application is distributed under the MIT license. For more information, refer to the [LICENSE](LICENSE) file.
