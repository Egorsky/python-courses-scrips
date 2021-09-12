import numpy as np
import os
import matplotlib.pyplot as plt
import cv2
import tensorflow as tf
import tensorflow.keras as keras
from tensorflow.keras import datasets, layers, models
from tensorflow.keras.callbacks import TensorBoard
import pickle
import time


NAME = "BL_Vishnevsky_vs_others-{}".format(int(time.time()))

DATADIR = r"Your_dir\spot_the_real_Vishnevsky\img"
CATEGORIES = ['Real Boris Lazarevich Vishnevsky', 'Not Vishnevsky']

IMG_SIZE = 80

new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
plt.imshow(new_array, cmap='gray')

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

X = X / 255.0

model = models.Sequential()
model.add(layers.Conv2D(64, (3,3), activation='relu', input_shape = X.shape[1:]))
model.add(layers.MaxPooling2D(3, 3))

model.add(layers.Conv2D(64, (3,3), activation='relu'))
model.add(layers.MaxPooling2D(2, 2))

model.add(layers.Flatten()) # this converts 3D feature matps into 1D feature labels

model.add(layers.Dense(32))
model.add(layers.Activation("relu"))

model.add(layers.Dense(1))
model.add(layers.Activation("sigmoid"))

model.compile(loss='binary_crossentropy',
            optimizer='adam',
            metrics=['accuracy'])

history = model.fit(X, y, batch_size=5, validation_split=0.24, epochs=9)

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

model.save('BLV-CNN.model')