import csv
import cv2
import numpy as np

lines = []
images = [] 
measurements = []
# Driving log file contains data of good driving behavior
# Loading that data from driving_log
with open('data/driving_log.csv') as csvfile:
  reader = csv.reader(csvfile)
  for line in reader:
    lines.append(line)

for line in lines: 
  for i in range(3):    
    source_path = line[i]
    filename = source_path.split('/')[-1]
    current_path = 'data/IMG/' + filename
    image = cv2.imread(current_path)
    images.append(image)
    # To have more data, using left and right images
    # by updating measurements
    if i ==0:
      measurements.append(float(line[3]))
    elif i == 1:
      measurements.append(float(line[3])+ 0.18)
    else:
      measurements.append(float(line[3]) - 0.18)

# Flipping images to augment the data
augmented_images, augmented_measurements = [], []
for image, measurement in zip(images,measurements):
  augmented_images.append(image)
  augmented_measurements.append(measurement)
  augmented_images.append(cv2.flip(image,1))
  augmented_measurements.append(measurement*-1.0)

X_train = np.array(augmented_images)
y_train = np.array(augmented_measurements)

from keras.models import Sequential
from keras.layers import Flatten, Dense, Activation, Convolution2D, Lambda, MaxPooling2D, Cropping2D

model = Sequential()
model.add(Lambda(lambda x: x/255.0 -0.5, input_shape=(160, 320, 3)))
# Cropping the image to avoid noise added by unnecessary part of image e.g. sky, trees
model.add(Cropping2D(cropping=((70,25), (0,0))))
model.add(Convolution2D(24, 5, 5, activation="relu"))
model.add(MaxPooling2D())
model.add(Convolution2D(36, 5, 5, activation="relu"))
model.add(MaxPooling2D())
model.add(Convolution2D(48, 5, 5, activation="relu"))
model.add(MaxPooling2D())
model.add(Convolution2D(64, 3, 3, border_mode='same', activation="relu"))
model.add(MaxPooling2D())
model.add(Convolution2D(64, 3, 3, border_mode='same', activation="relu"))
model.add(MaxPooling2D())
model.add(Flatten())
model.add(Dense(1164))
model.add(Activation('relu'))
model.add(Dense(100))
model.add(Activation('relu'))
model.add(Dense(50))
model.add(Activation('relu'))
model.add(Dense(10))
model.add(Activation('relu'))
model.add(Dense(1))

# Using adam optimizer
model.compile(loss='mse', optimizer='adam')
model.fit(X_train, y_train, validation_split=0.2, shuffle=True, nb_epoch=3)

model.save('model.h5')
