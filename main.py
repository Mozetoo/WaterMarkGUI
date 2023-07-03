from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont
import os


# adds watermark at the top center and bottom and saves it in a directory
def add_watermark(image_path, watermark_text, output_dir):
    # Open the image
    image = Image.open(image_path)
    # Create a copy of the image to draw the watermark on
    watermarked_image = image.copy()
    # Calculate the position for the watermark (in this case, centered)
    image_width, image_height = watermarked_image.size
    # Draw on Image
    draw = ImageDraw.Draw(watermarked_image)
    # Font Size
    font_size = int(image_width / 20)
    # Define the watermark text font and size
    font = ImageFont.truetype("arial.ttf", font_size)
    # Calculate position of the top left watermark
    top_left_position = (10, 10)
    # Draw the watermark at the top left corner
    draw.text(top_left_position, watermark_text, font=font, fill=(255, 255, 255, 128))
    # Calculate the position for the watermark at the middle
    middle_position = (image_width - 350, image_height - 250)
    # Draw the watermark at the middle
    draw.text(middle_position, watermark_text, font=font, fill=(255, 255, 255, 128))
    # Calculate the position for the watermark at the bottom right corner
    bottom_right_position = (image_width - 150, image_height - 50)
    # Draw the watermark at the bottom right corner
    draw.text(bottom_right_position, watermark_text, font=font, fill=(255, 255, 255, 128))
    # Save the watermarked image
    output_filename = os.path.basename(image_path)  # Use the same filename as the original image
    output_path = os.path.join(output_dir, output_filename)
    # Save the watermarked image to the output path
    watermarked_image.save(output_path)
    watermarked_image.show()


# starts the adding watermark process
def upload_image():
    # Open a file dialog to choose an image file
    filetype = (
        ('image files - jpg', '*.jpg'),
        ('image files - png', '*.png'),
        ('all files', '*.*'),
    )   # displaying filetypes to choose from on the dialog box

    image_path = filedialog.askopenfilename(initialdir="/Users/zetop/Pictures", title='Select Image',
                                            filetypes=filetype)

    if image_path:
        # Add watermark to the selected image
        watermark_text = "@justzeto"  # shouldnt be more than 9 characters
        output_dir = "/Users/zetop/Pictures/LOGO/watermark"  # Change the output path as per your requirement

        add_watermark(image_path, watermark_text, output_dir)

        # Show a success message
        result_label.config(text="Image watermarked successfully!")


window = Tk()
window.title("Image Watermarking")
window.geometry("400x200")

# Create a label to display the result
result_label = Label(window, text="")
result_label.pack(pady=20)

# Create a button to upload an image
upload_button = Button(window, text="Upload Image", command=upload_image)
upload_button.pack()

# Start the Tkinter event loop
window.mainloop()
