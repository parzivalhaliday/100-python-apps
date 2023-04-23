# Image Resizer
Image Resizer is a Python script that allows you to reduce the size of an image file by resizing it and changing its quality. It supports the following file formats: JPG, JPEG, and PNG.

![image](https://github.com/parzivalhaliday/python-apps/blob/main/zip/image.png)

## Installation
To use the script, you need to have Python 3.x installed on your computer. If you don't have Python installed, you can download it from the [official website](https://www.python.org/downloads/).

After installing Python, you need to install the required Python packages. You can do this by running the following command in your terminal:


```python 
pip install -r requirements.txt
```

This will install the `pillow` and `tkinter` packages, which are needed to run the script.

## IUsage
To use the script, follow these steps:

1. Open a terminal and navigate to the directory where the script is located.

2. Run the script using the following command:

```python
py image_resizer.py
```

3. A file selection dialog will appear. Choose the image file you want to resize.

4. Enter the target size (in KB) and quality (in percentage) values when prompted. You can also choose to resize the image based on a target width and height, or choose to only reduce the file size without changing the image dimensions.

5. If the size of the selected file is greater than the target size, a new file with the reduced size will be saved in the same directory as the original file, with "_reduced" added to the filename.

6. You can choose to preview the resized image before saving it by selecting the preview option.

7. You can also choose to process multiple files at once by selecting the batch processing option.

## Options
The following options are available when running the script:

- Target Size: Enter the target size (in KB) for the resized image. The script will attempt to reduce the file size to the specified value by adjusting the image quality and/or dimensions.

- Quality: Enter the desired quality (in percentage) for the resized image. The higher the quality, the larger the file size will be.

- Width: Enter the desired width (in pixels) for the resized image. The script will adjust the image dimensions to fit within the specified width while maintaining the aspect ratio.

- Height: Enter the desired height (in pixels) for the resized image. The script will adjust the image dimensions to fit within the specified height while maintaining the aspect ratio.

- Preview: Choose to preview the resized image before saving it.

- Batch Processing: Choose to process multiple files at once. A file selection dialog will appear where you can choose one or more files to process.

Requirements
- Python 3.x
- pillow==8.4.0
- tkinter==8.6

The `pillow` package is used for image processing, and `tkinter` is used to create the file selection dialog and preview window. These packages can be installed using the 
`pip install -r requirements.txt`

command in the terminal.
