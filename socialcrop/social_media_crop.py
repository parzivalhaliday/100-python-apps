from PIL import Image as PILImage
import os
from tkinter import *
from tkinter import filedialog, messagebox
from typing import Tuple

class SocialMediaCropper:
    # Standard sizes for social media platforms
    SIZES = {
        "Instagram Square": (1080, 1080),
        "Instagram Story": (1080, 1920),
        "Facebook Post": (1200, 630),
        "Twitter Post": (1200, 675),
        "LinkedIn Cover": (1584, 396),
        "YouTube Thumbnail": (1280, 720)
    }

    def __init__(self):
        self.window = Tk()
        self.window.title("Social Media Photo Editor")
        self.window.geometry("600x400")
        self.setup_ui()

    def setup_ui(self):
        # File selection button
        Button(self.window, text="Select Photo", command=self.select_image).pack(pady=10)
        
        # Platform selection list
        Label(self.window, text="Select Platform:").pack()
        self.platform_var = StringVar(self.window)
        self.platform_var.set(list(self.SIZES.keys())[0])
        OptionMenu(self.window, self.platform_var, *self.SIZES.keys()).pack()

        # Convert button
        Button(self.window, text="Convert", command=self.crop_image).pack(pady=10)

    def select_image(self):
        self.image_path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif *.webp")]
        )
        if self.image_path:
            messagebox.showinfo("Success", "Photo selected!")

    def resize_image(self, image: PILImage.Image, target_size: Tuple[int, int]) -> PILImage.Image:
        # Preserve aspect ratio
        target_ratio = target_size[0] / target_size[1]
        img_ratio = image.width / image.height

        if img_ratio > target_ratio:
            # Image is too wide, scale by height
            new_height = target_size[1]
            new_width = int(new_height * img_ratio)
        else:
            # Image is too tall, scale by width
            new_width = target_size[0]
            new_height = int(new_width / img_ratio)

        resized = image.resize((new_width, new_height), PILImage.LANCZOS)
        
        # Center and crop
        left = (resized.width - target_size[0]) // 2
        top = (resized.height - target_size[1]) // 2
        right = left + target_size[0]
        bottom = top + target_size[1]

        return resized.crop((left, top, right, bottom))

    def crop_image(self):
        if not hasattr(self, 'image_path'):
            messagebox.showerror("Error", "Please select a photo first!")
            return

        try:
            # Get dimensions for selected platform
            platform = self.platform_var.get()
            target_size = self.SIZES[platform]

            # Open and edit image
            with PILImage.open(self.image_path) as img:
                resized_img = self.resize_image(img, target_size)

                # Choose save location
                save_path = filedialog.asksaveasfilename(
                    defaultextension=".jpg",
                    filetypes=[("JPEG files", "*.jpg")],
                    initialfile=f"{platform.lower().replace(' ', '_')}_cropped.jpg"
                )

                if save_path:
                    resized_img.save(save_path, "JPEG", quality=95)
                    messagebox.showinfo("Success", "Photo saved successfully!")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    app = SocialMediaCropper()
    app.window.mainloop() 