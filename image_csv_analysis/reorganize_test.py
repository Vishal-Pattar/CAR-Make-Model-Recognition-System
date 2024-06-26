import os
import shutil
import pandas as pd
from PIL import Image

# Read the CSV file
df = pd.read_csv("./test_data.csv")

# Create directory for preprocessed images
preprocessed_dir = "../preprocessed_dataset/test"
if not os.path.exists(preprocessed_dir):
    os.makedirs(preprocessed_dir)

# Iterate through each row of the dataframe
for index, row in df.iterrows():
    # Extract class name, file path, and bounding box coordinates
    file_path = row['file_name']
    bbox_x1, bbox_y1, bbox_x2, bbox_y2 = row['bbox_x1'], row['bbox_y1'], row['bbox_x2'], row['bbox_y2']

    # Open image using PIL
    image = Image.open(file_path)

    # Crop image based on bounding box coordinates
    cropped_image = image.crop((bbox_x1, bbox_y1, bbox_x2, bbox_y2))

    # Extract file name from the file path
    file_name = os.path.basename(file_path)

    # Construct destination file path
    destination_path = os.path.join(preprocessed_dir, file_name)

    # Save cropped image
    cropped_image.save(destination_path)

print("Images cropped and saved successfully.")
