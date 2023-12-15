# One-Time Password (OTP) Generator

This Python script generates a One-Time Password (OTP) using the TOTP (Time-based One-Time Password) algorithm with a shared secret.

![image](https://github.com/parzivalhaliday/100-python-apps/blob/main/totpgenarator/image.png)


## Requirements

- Python 3.x
- Install required libraries:

```python
pip install pyotp pyperclip
```
## Usage

1) Run the script:

```python
py otp_generator.py
```

2) Enter the shared secret when prompted.

3) The script will generate and display a one-time password.

4) The password is automatically copied to the clipboard.

## Notes
- Ensure that the pyotp and pyperclip libraries are installed before running the script.

- Keep the shared secret secure and do not share it with others.

- Use the generated OTP for authentication purposes.

# Features

- **OTP Generation**: Quickly generate One-Time Passwords (OTPs) using the TOTP algorithm.
  
- **Clipboard Integration**: Automatically copies the generated OTP to the clipboard for easy paste.

- **User-Friendly**: Simple command-line interface that prompts the user for the shared secret and provides clear instructions.

- **Secure**: Utilizes the `pyotp` library to implement Time-based One-Time Passwords, enhancing security.

- **Dependency Management**: Easily install dependencies using the provided requirements file.

## Planned Features

- **Multi-Factor Authentication (MFA) Support**: Enhance security by supporting multi-factor authentication workflows.

- **GUI Interface**: Develop a graphical user interface for a more user-friendly experience.

- **Configuration File Support**: Allow users to store and manage multiple shared secrets in a configuration file.

- **Error Handling**: Implement robust error handling for various scenarios.

Feel free to suggest additional features or improvements by opening an issue or contributing to the project.


## Contributing
Contributions are welcome! If you have any ideas for features or improvements, feel free to submit a pull request or open an issue. 

## License
You can use the code however you want.
