import os
import csv

def count_images_in_folders(dataset_path):
    folders = [f.path for f in os.scandir(dataset_path) if f.is_dir()]
    data = []

    for folder in folders:
        class_name = os.path.basename(folder)
        images = [f.name for f in os.scandir(folder) if f.is_file() and f.name.endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp'))]
        data.append({'type': 'train', 'class': class_name, 'image_count': len(images)})

    return data

def save_to_csv(data, csv_filename):
    with open(csv_filename, 'w', newline='') as csvfile:
        fieldnames = ['type', 'class', 'image_count']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for row in data:
            writer.writerow(row)

# Replace 'dataset_path' with the path to your dataset
dataset_path = './preprocessed_dataset/train'
csv_filename = 'image_counts.csv'

data = count_images_in_folders(dataset_path)
save_to_csv(data, csv_filename)
