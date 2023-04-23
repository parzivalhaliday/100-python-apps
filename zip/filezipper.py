import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from PIL import Image

# Open a file selection window for the user to choose a file
root = Tk()
root.withdraw()  # Hide the main window to avoid displaying a visible window
file_path = askopenfilename()  # Open a file selection dialog
if not file_path:  # If the user didn't select a file, exit
    exit()

# Get target size and quality values from the user
target_size = int(input("Target size (KB): "))
quality = int(input("Quality (%): "))

# Split the file path into directory, filename, and extension
directory, filename = os.path.split(file_path)
extension = os.path.splitext(filename)[1].lower()

# Check if the selected file is of a supported type
if extension in (".jpg", ".jpeg", ".png"):
    # Open the image file using the PIL library
    with Image.open(file_path) as img:
        # Get the current size of the image
        current_size = os.path.getsize(file_path) // 1024
        # Check if the current size is greater than the target size
        if current_size > target_size:
            # Resize the image using PIL's thumbnail function
            width, height = img.size
            new_width = int(width * (target_size / current_size) ** 0.5)
            new_height = int(height * (target_size / current_size) ** 0.5)
            img.thumbnail((new_width, new_height))
            # Set the image quality
            img.save(os.path.join(directory, f"{os.path.splitext(filename)[0]}_reduced{extension}"), quality=quality)
        else:
            # If the file size is smaller than or equal to the target size, print a message
            print("The file size is smaller than or equal to the target size.")
else:
    # If the file type is not supported, print a message
    print("The file type is not supported.")
