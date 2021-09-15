import numpy as np
import os
import sys
import matplotlib.pyplot as plt
import cv2
import tensorflow as tf
import tensorflow.keras as keras
from tensorflow.keras import datasets, layers, models
from tensorflow.keras.callbacks import TensorBoard
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator
from skimage import io
from PIL import Image
import pickle
import time

NAME = "BL_Vishnevsky_vs_others-{}".format(int(time.time()))

DATADIR = r"Your_dir\spot_the_real_Vishnevsky\img"
CATEGORIES = ['The Real Boris Lazarevich Vishnevsky', 'Not Vishnevsky']

for category in CATEGORIES:
    path = os.path.join(DATADIR, category)
    for img in os.listdir(path):
        img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
        plt.imshow(img_array, cmap="gray")
        plt.show()
        break
    break

# Data augmentation for both datasets

# Folder with target images

gen = ImageDataGenerator(rotation_range=10, width_shift_range=0.15,
                        height_shift_range=0.1, shear_range=0.15,
                        zoom_range=0.12, channel_shift_range=10., horizontal_flip=True,
                        brightness_range=[0.3,0.9], fill_mode='nearest')

image_path = r'Your_dir\spot_the_real_Vishnevsky\img\The Real Boris Lazarevich Vishnevsky'
os.chdir(image_path)

j = 1
for img in os.listdir(image_path):
    im = Image.open(img)
    rgb_im = im.convert('RGB')
    rgb_im.save(img)
    j += 1


# Obtaining image
for img in os.listdir(image_path):
    image = io.imread(img, plugin='matplotlib')
    image = image.reshape((-1, ) + image.shape)

    i = 0
    for batch in gen.flow(image, batch_size=16,
                          save_to_dir=image_path,
                          save_prefix='aug',
                          save_format='jpg'):
        i += 1
        if i > 6:
            break

# Folder with images that program need to detect as not-target ones

gen = ImageDataGenerator(rotation_range=10, width_shift_range=0.1,
                        height_shift_range=0.15, shear_range=0.1,
                        zoom_range=0.1, channel_shift_range=10., horizontal_flip=True,
                        brightness_range=[0.3,0.9], fill_mode='nearest')

image_path = r'Your_dir\spot_the_real_Vishnevsky\img\Not Vishnevsky'
os.chdir(image_path)

j = 1
for img in os.listdir(image_path):
    im = Image.open(img)
    rgb_im = im.convert('RGB')
    rgb_im.save(img)
    j += 1


# Obtaining image
for img in os.listdir(image_path):
    #if img.endswith(".jpg"):
    image = io.imread(img, plugin='matplotlib')
    image = image.reshape((-1, ) + image.shape)

    i = 0
    for batch in gen.flow(image, batch_size=16,
                          save_to_dir=image_path,
                          save_prefix='aug',
                          save_format='jpg'):
        i += 1
        if i > 6:
            break

os.chdir(r'Your_dir\spot_the_real_Vishnevsky')
cwd = os.getcwd()
print("Current working directory: {0}".format(cwd))

IMG_SIZE = 80

new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
plt.imshow(new_array, cmap='gray')
plt.show()

training_data = []

def create_training_data():
    for category in CATEGORIES:
        path = os.path.join(DATADIR, category)
        class_num = CATEGORIES.index(category)
        for img in os.listdir(path):
            try:
                img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
                IMG_SIZE = 80
                new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
                training_data.append([new_array, class_num])
            except Exception as e:
                pass

create_training_data()

import random

random.shuffle(training_data)

X = []
y = []

for features, label in training_data:
    X.append(features)
    y.append(label)
    
X = np.array(X).reshape(-1, IMG_SIZE, IMG_SIZE, 1)
y = np.array(y)

import pickle

pickle_out = open("X.pickle","wb")
pickle.dump(X, pickle_out)
pickle_out.close()

pickle_out = open("y.pickle","wb")
pickle.dump(y, pickle_out)
pickle_out.close()

pickle_in = open('X.pickle', 'rb')
X = pickle.load(pickle_in)
pickle_in = open('y.pickle', 'rb')
y = pickle.load(pickle_in)

X = X / 255.0

# Neural network

model = models.Sequential()
model.add(layers.Conv2D(64, (3,3), activation='relu', input_shape = X.shape[1:]))
model.add(layers.MaxPooling2D(3, 3))

model.add(layers.Conv2D(32, (3,3), activation='relu'))
model.add(layers.MaxPooling2D(2, 2))

model.add(layers.Flatten()) # this converts 3D feature matps into 1D feature labels

model.add(layers.Dense(64))
model.add(layers.Activation("relu"))

model.add(layers.Dense(1))
model.add(layers.Activation("sigmoid"))

model.compile(loss='binary_crossentropy',
            optimizer='adam',
            metrics=['accuracy'])

history = model.fit(X, y, batch_size=4, validation_split=0.3, epochs=5)

test_loss, test_acc = model.evaluate(X, y, verbose=2)
print('Accuracy is:', test_acc)

plt.plot(history.history['accuracy'], label='accuracy')
plt.plot(history.history['val_accuracy'], label = 'val_accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.ylim([0.2, 1])
plt.legend(loc='lower right')

test_loss, test_acc = model.evaluate(X,  y, verbose=2)

plt.plot(history.history['val_loss'], label = 'val_loss', color='green')
plt.plot(history.history['loss'], label = 'loss', color='red')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.ylim([0.0, 1])
plt.legend(loc='lower right')

test_loss, test_val_loss = model.evaluate(X,  y, verbose=2)

os.chdir(r'Your_dir\spot_the_real_Vishnevsky')
model.save('BLV-CNN.model')