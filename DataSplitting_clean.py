# %%
import os
import shutil
import random
from tqdm import tqdm

source_directory = "COVID-19_Radiography_Dataset"
classes = ["COVID", "Normal"]

# Destination
destination_directory = "covid_normal_split"

splits = ["train", "val", "test"]
split_ratios = [0.7, 0.15, 0.15]  # 70% train, 15% val, 15% test

for cls in classes:
    img_directory = os.path.join(source_directory, cls, "images")
    img_files = os.listdir(img_directory)
    random.shuffle(img_files)

    # Create split indexes
    train_split = int(len(img_files) * split_ratios[0])
    val_split = int(len(img_files) * (split_ratios[0] + split_ratios[1]))

    split_data = {
        "train": img_files[:train_split],
        "val": img_files[train_split:val_split],
        "test": img_files[val_split:]
    }

    # Create folders and copy files
    for split in splits:
        target_dir = os.path.join(destination_directory, split, cls)
        os.makedirs(target_dir, exist_ok=True)

        for filename in tqdm(split_data[split], desc=f"Copying {split} data for class {cls}"):
            source_path = os.path.join(img_directory, filename)
            destination_path = os.path.join(target_dir, filename)
            shutil.copy2(source_path, destination_path)




