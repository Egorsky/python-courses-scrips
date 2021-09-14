import cv2
import os
import tensorflow as tf
import matplotlib.pyplot as plt
from keras.preprocessing import image
import matplotlib.image as mpimg
import numpy as np


CATEGORIES = ['The Real Boris Lazarevich Vishnievsky', 'Not Vishnievsky']


def prepare(filepath):
    IMG_SIZE = 80
    img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
    return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)

# loading model
model = tf.keras.models.load_model("BLV-CNN.model")

DATADIR = r'Your_dir\spot_the_real_Vishnevsky\manual_testing'


i = 1
for item in os.listdir(DATADIR):
    prediction = model.predict([prepare(r'Your_dir\spot_the_real_Vishnevsky\manual_testing\{}.jpg'.format(i))])
    img = mpimg.imread(r'Your_dir\spot_the_real_Vishnevsky\manual_testing\{}.jpg'.format(i))
    imgplot = plt.imshow(img)
    plt.show()

    print(CATEGORIES[int(prediction[0][0])])
    i += 1 

