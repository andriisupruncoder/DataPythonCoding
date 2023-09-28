from tkinter import *
from tkinter import filedialog
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
import piexif

root = Tk()
root.title("Edit Photo Metadata")

# Function to choose an image
def choose_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
    image_file_entry.delete(0, END)
    image_file_entry.insert(0, file_path)

# Function to save changes to the metadata
def save_changes():
    image_file_path = image_file_entry.get()
    created = created_entry.get()
    modified = modified_entry.get()
    content = content_entry.get()

    # Load image and its EXIF data
    image = Image.open(image_file_path)
    exif_dict = piexif.load(image.info["exif"])

    # Modify the necessary fields (using sample tags, ensure correct ones for your use case)
    # The below 0x9003, 0x9004, 0x010e are example tags for DateTimeOriginal, DateTimeDigitized, and ImageDescription respectively.
    exif_dict["0th"][0x9003] = created
    exif_dict["0th"][0x9004] = modified
    exif_dict["0th"][0x010e] = content.encode()

    exif_bytes = piexif.dump(exif_dict)
    image.save(image_file_path, exif=exif_bytes)

# GUI Layout
image_file_label = Label(root, text="Image file path:")
image_file_label.grid(row=0, column=0)

image_file_entry = Entry(root, width=40)
image_file_entry.grid(row=0, column=1)

choose_button = Button(root, text="Choose Image", command=choose_image)
choose_button.grid(row=0, column=2)

created_label = Label(root, text="Created:")
created_label.grid(row=1, column=0)
created_entry = Entry(root)
created_entry.grid(row=1, column=1)

modified_label = Label(root, text="Modified:")
modified_label.grid(row=2, column=0)
modified_entry = Entry(root)
modified_entry.grid(row=2, column=1)

content_label = Label(root, text="Content:")
content_label.grid(row=3, column=0)
content_entry = Entry(root)
content_entry.grid(row=3, column=1)

save_button = Button(root, text="Save Changes", command=save_changes)
save_button.grid(row=4, column=1)

root.mainloop()
