# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 11:50:11 2020

@author: guruji0
"""


from keras.preprocessing.image import img_to_array
from keras.models import load_model
import numpy as np
import argparse
import imutils
import pickle
import time
import cv2
import os


print("[INFO] loading liveness detector...")
model = load_model("detector.model")
le = pickle.loads(open("le.pickle", "rb").read())


image = cv2.imread("Your input image")

img = cv2.resize(image, (32, 32))
img = img.astype("float") / 255.0
img = img_to_array(img)
img = np.expand_dims(img, axis=0)
# pass the imagethrough the trained rotation detector
# model to determine the rotation angle
preds = model.predict(img)[0]
j = np.argmax(preds)
label = le.classes_[j]

print(label)