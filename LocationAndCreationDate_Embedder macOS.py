import os
import tkinter as tk
from tkinter import filedialog
import subprocess
import shutil

# Create a GUI window to select the input file and output folder or file
root = tk.Tk()
root.withdraw()  # Hide the main window

# Ask the user to select the input file (video or image)
input_file = filedialog.askopenfilename(title="Select Input File", filetypes=[("Video/Image Files", "*.mp4 *.mov *.avi *.jpg *.png")])

# Check if an input file was selected
if not input_file:
    print("No input file selected. Exiting.")
    exit()

# Ask the user to select the output folder or file
output_selection = filedialog.askdirectory(title="Select Output Folder")  # Change this to ask for a folder or file

# Check if an output folder or file was selected
if not output_selection:
    print("No output folder or file selected. Exiting.")
    exit()

# Function to embed metadata from input file to output file
def embed_metadata(input_path, output_path):
    try:
        # Use exiftool to copy metadata from input file to output file
        subprocess.run(["exiftool", "-overwrite_original", "-TagsFromFile", input_path, output_path])
        print("Metadata embedded successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Check if the selected output is a folder or a file
if os.path.isdir(output_selection):
    # If the output is a folder, create the "exported_images" subfolder
    folder_name = os.path.basename(input_file)
    exported_images_folder = os.path.join(output_selection, f"{folder_name}_exported_images")
    os.makedirs(exported_images_folder, exist_ok=True)

    # Embed metadata and modify creation and modified dates for all files in the output folder
    for root, dirs, files in os.walk(output_selection):
        for file in files:
            input_path = input_file
            output_path = os.path.join(root, file)
            
            # Check if the file is an image
            if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
                try:
                    embed_metadata(input_path, output_path)
                    creation_date = os.path.getctime(input_file)
                    modified_date = os.path.getmtime(input_file)
                    os.utime(output_path, (creation_date, modified_date))
                except Exception as e:
                    print(f"An error occurred while processing {file}: {str(e)}")

    print("Metadata embedded and dates modified for all image files in the output folder.")
else:
    # If the output is a single file, embed metadata and modify creation and modified dates
    output_file = output_selection
    try:
        embed_metadata(input_file, output_file)
        creation_date = os.path.getctime(input_file)
        modified_date = os.path.getmtime(input_file)
        os.utime(output_file, (creation_date, modified_date))
        print("Metadata embedded and dates modified for the output file.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
