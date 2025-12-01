# %%
# Imports
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os
import glob
from PIL import Image

# %%
# Import: Images 

def import_images(path):
    images = []
    for file in glob.glob(path):
        img = Image.open(file, 'r')
        img = img.resize((256, 256))
        img = np.array(img)
        IMG = img.ravel()
        images.append(IMG)

    return images

# Normal Xray Images
normal_images_path = "COVID-19_Radiography_Dataset/Normal/images/*.png"
normal_images_arr = import_images(normal_images_path)
print(len(normal_images_arr))

# COVID Xray Images
covid_images_path = "COVID-19_Radiography_Dataset/COVID/images/*.png"
covid_images_arr = import_images(covid_images_path)
print(len(covid_images_arr))


# %%
# Imports

import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing.image import ImageDataGenerator




