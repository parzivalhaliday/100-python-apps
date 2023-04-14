from PIL import Image
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog
import os

# Show a file selection dialog to choose an image file
root = tk.Tk()
root.withdraw()  # Hide the main window
file_path = filedialog.askopenfilename(title="Select an Image File", filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])

# Open the selected image file using the Pillow library
try:
    image = Image.open(file_path)
except:
    print("Error: Unsupported file type or cannot open the file.")
else:
    # Get a list of (count, color) tuples representing the colors in the image
    # and sort them by count to get the most common colors first
    colors = image.getcolors(image.size[0] * image.size[1])
    most_common_colors = sorted(colors, key=lambda x: x[0], reverse=True)[:10]

    # Extract the color names and pixel counts from the most common colors list
    color_names = [f"#{color[1][0]:02x}{color[1][1]:02x}{color[1][2]:02x}" for color in most_common_colors]
    pixel_counts = [color[0] for color in most_common_colors]

    # Create a bar plot of the top 10 colors and their pixel counts
    fig, ax = plt.subplots(figsize=(10, 5))
    bars = ax.bar(color_names, pixel_counts, color=color_names)

    # Add the pixel counts as annotations to the top of each bar in the plot
    for bar, count in zip(bars, pixel_counts):
        ax.annotate(str(count), xy=(bar.get_x() + bar.get_width() / 2, bar.get_height()), ha='center', va='bottom')

    # Add labels and a title to the plot
    ax.set_xlabel('Color Code')
    ax.set_ylabel('Pixel Count')
    ax.set_title(f"{os.path.basename(file_path)} - Top 10 Colors")

    # Rotate the x-axis labels and align them to the right for better readability
    plt.xticks(rotation=45, ha='right')

    # Show the plot
    plt.show()
