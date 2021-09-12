import cv2
import os
import tensorflow as tf
import matplotlib.pyplot as plt
from keras.preprocessing import image
import matplotlib.image as mpimg
import numpy as np


CATEGORIES = ['Real Boris Lazarevich Vishnevsky', 'Not Vishnevsky']


def prepare(filepath):
    IMG_SIZE = 80
    img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
    return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)

# loading model
model = tf.keras.models.load_model("BLV-CNN.model")

DATADIR = r'C:\\Users\\egoog\\Documents\\Coding\\spot_the_real_Vishnevsky\\manual_testing'

prediction = model.predict([prepare(r'C:\Users\egoog\Documents\Coding\spot_the_real_Vishnevsky\manual_testing\2.jpg')])
img = mpimg.imread(r'C:\Users\egoog\Documents\Coding\spot_the_real_Vishnevsky\manual_testing\2.jpg')
imgplot = plt.imshow(img)
plt.show()

print(CATEGORIES[int(prediction[0][0])])

prediction = model.predict([prepare(r'C:\Users\egoog\Documents\Coding\spot_the_real_Vishnevsky\manual_testing\3.jpg')])
img = mpimg.imread(r'C:\Users\egoog\Documents\Coding\spot_the_real_Vishnevsky\manual_testing\3.jpg')
imgplot = plt.imshow(img)
plt.show()

print(CATEGORIES[int(prediction[0][0])])

prediction = model.predict([prepare(r'C:\Users\egoog\Documents\Coding\spot_the_real_Vishnevsky\manual_testing\4.jpg')])
img = mpimg.imread(r'C:\Users\egoog\Documents\Coding\spot_the_real_Vishnevsky\manual_testing\4.jpg')
imgplot = plt.imshow(img)
plt.show()

print(CATEGORIES[int(prediction[0][0])])

