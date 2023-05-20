import os
from tkinter import Tk, filedialog

# Function to merge two files
def merge_files(file1, file2, target_file):
    # Open the first file in binary mode and read its content
    with open(file1, 'rb') as f1:
        content1 = f1.read()

    # Open the second file in binary mode and read its content
    with open(file2, 'rb') as f2:
        content2 = f2.read()

    # Concatenate the contents of the two files with a newline character in between
    merged_content = content1 + b'\n' + content2

    # Open the target file in binary mode and write the merged content
    with open(target_file, 'wb') as target:
        target.write(merged_content)

# Select a PNG file using a file dialog
Tk().withdraw()
png_file = filedialog.askopenfilename(title="Select PNG File", filetypes=(("PNG Files", "*.png"),))

if png_file:  # If a PNG file is selected, proceed
    answer = input("Do you want to create a new TXT file or select an existing TXT file? (Type 'c' for create, 's' for select): ")

    if answer.lower() == 'c':
        # Create a new text file and prompt the user for the text to append
        text = input("Enter the text you want to append at the end of the image: ")
        txt_file = 'new.txt'
        with open(txt_file, 'w') as f:
            f.write(text)
    elif answer.lower() == 's':
        # Select an existing text file using a file dialog
        Tk().withdraw()
        txt_file = filedialog.askopenfilename(title="Select TXT File", filetypes=(("Text Files", "*.txt"),))
    else:
        print("Invalid option. Exiting the program.")
        exit()

    target_file = 'merged_file.png'

    # Merge the selected PNG and TXT files into the target file
    merge_files(png_file, txt_file, target_file)

    # Get the size of the merged file
    size = os.path.getsize(target_file)

    print(f"{png_file} and {txt_file} are successfully merged, and {target_file} is created.")
    print(f"Size of the merged file: {size} bytes.")
else:
    print("No PNG file selected. Exiting the program.")
