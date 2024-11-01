from PIL import Image
import os

# Set the folder path where your images are stored
folder_path = "ACC_UNet_V2/ACC_UNet_V2/Experiments/datasets/ISIC18_exp1/Test_Folder/labelcol/labelcol"

# Loop through all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith("_segmentation.png"):  # Check for segmentation PNGs
        # Generate the new filename by removing '_segmentation' and changing to .jpg
        new_filename = filename.replace("_segmentation.png", ".jpg")

        # Open the image, convert it to RGB, and save as .jpg with the new name
        img = Image.open(os.path.join(folder_path, filename)).convert("RGB")
        img.save(os.path.join(folder_path, new_filename), "JPEG")

        # Optionally, delete the original .png file
        os.remove(os.path.join(folder_path, filename))

print("Conversion, renaming, and cleanup completed.")
