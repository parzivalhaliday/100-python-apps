import os

# get the file name from user input
file_name = input("Enter file name with extension: ")

# get the file extension
file_extension = os.path.splitext(file_name)[1]

# ask if content should be added to the file
add_content = input("Do you want to add content to the file? (yes or no): ")

# if user wants to add content, ask for content
if add_content.lower() == "yes":
    file_content = input("Enter the content for the file:\n")
else:
    # if user does not want to add content, use default content based on file extension
    if file_extension == ".txt":
        file_content = "This is a test file."
    elif file_extension == ".py":
        file_content = "print('This file was automatically generated.')"
    elif file_extension == ".js":
        file_content = "console.log('This file was automatically generated.');"
    elif file_extension == ".html":
        file_content = "<html><body><h1>This file was automatically generated.</h1></body></html>"
    elif file_extension == ".css":
        file_content = "body { background-color: lightblue; }"
    else:
        file_content = "This is a test file."

# create the file and write the content
with open(file_name, "w") as file:
    file.write(file_content)

# ask if user wants to save the file
save_file = input("Do you want to save the file? (yes or no): ")

# if user wants to save the file, do nothing
if save_file.lower() == "yes":
    pass
else:
    # if user does not want to save the file, delete the file
    os.remove(file_name)
