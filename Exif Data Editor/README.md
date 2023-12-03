# Exif Data Editor

Exif Data Editor is a Python program that allows you to merge various types of image files (such as PNG, JPEG, and GIF) with a text file. The merged file can be useful for adding annotations, captions, or metadata to images.

![exiddataeditor](https://github.com/parzivalhaliday/100-python-apps/blob/main/Exif%20Data%20Editor/image.png)

## Requirements

- Python 3.x
- Tkinter library (usually included with Python)

## Features

- **Support for Multiple Image Formats:** Exif Data Editor supports popular image formats such as PNG, JPEG, and GIF, allowing you to merge text with different types of images.

- **Text File Creation or Selection:** You can choose to create a new text file within the program and enter the desired text, or select an existing text file using the file dialog.

- **Merge and Output:** The program seamlessly merges the selected image and text file, creating a new merged file. The merged file retains the image format of the original file.

- **File Size Calculation:** After merging the files, the program provides information about the size of the merged file in bytes, giving you an idea of the resulting file's storage requirements.

## Usage

1. Run the program by executing the script `exifdataeditor.py`.

2. Select an image file (PNG, JPEG, or GIF) using the file dialog that opens.

3. Choose one of the following options:
    - Type 'c' to create a new text file and enter the desired text to append at the end of the image.
    - Type 's' to select an existing text file using the file dialog.

4. If you chose to create a new text file, enter the desired text when prompted.

5. If you chose to select an existing text file, choose the file using the file dialog.

6. The program will merge the image and text file, creating a new file named `merged_file.<image_extension>`.

7. The program will display a message indicating the successful merging process and the size of the merged file in bytes.

## Contributing
Contributions are welcome! If you have any ideas for features or improvements, feel free to submit a pull request or open an issue.


## License
You can use the code however you want.