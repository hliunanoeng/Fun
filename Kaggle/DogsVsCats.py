import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten,Conv2D, MaxPooling2D
from tensorflow.keras.callbacks import TensorBoard
import matplotlib.pyplot as plt
import numpy as np
import time
import os
import cv2
import random
import pickle

# pet image classification

# datadir = "/Users/hliu/Desktop/PetImages"
categories = ["Dog","Cat"]

#check out the images

# for category in categories:
#     path = os.path.join(datadir, category)
#     for img in os.listdir(path):
#         img_array = cv2.imread(os.path.join(path,img),cv2.IMREAD_GRAYSCALE)
#         #plt.imshow(img_array, cmap="gray")
#         #plt.show()
#         break
#     break

#make all images the same shape
# img_size=100
# new_array= cv2.resize(img_array, (img_size,img_size))
#plt.imshow(new_array, cmap="gray")
#plt.show()

#create training data

# training_data = []
# img_size=100
#
# def compile_traning_data():
#     for category in categories:
#         path = os.path.join(datadir, category)
#         class_num = categories.index(category)
#         for img in os.listdir(path):
#             try:
#                 img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
#                 new_array = cv2.resize(img_array,(img_size,img_size))
#                 training_data.append([new_array,class_num])
#             except Exception as e:
#                 pass
#
# compile_traning_data()
# random.shuffle(training_data)
#
# X = []
# y = []
#
# for features, label in training_data:
#     X.append(features)
#     y.append(label)
#
# X = np.array(X).reshape(-1,img_size,img_size,1) #-1 stands for the unknown dimension

#save the data

# pickle_out = open("X.pickle","wb")
# pickle.dump(X,pickle_out)
# pickle_out.close()
#
# pickle_out = open("y.pickle","wb")
# pickle.dump(y,pickle_out)
# pickle_out.close()

pickle_in = open("X.pickle","rb")
X = np.asarray(pickle.load(pickle_in))

pickle_in = open("y.pickle","rb")
y = np.asarray(pickle.load(pickle_in))

#normalize data
x= X/255.0

#otherwise tensorflow will not work for macos
os.environ['KMP_DUPLICATE_LIB_OK']='True'

# build model and add layers

def modelBuilder(dense_layer, layer_size, conv_layer, NAME):
    tensorboard = TensorBoard(log_dir='\logs/{}'.format(NAME))

    model = Sequential()

    model.add(Conv2D(layer_size, (3, 3), input_shape=X.shape[1:]))
    model.add(Activation("relu"))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    for i in range(conv_layer - 1):
        model.add(Conv2D(layer_size, (3, 3)))
        model.add(Activation("relu"))
        model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Flatten())

    for i in range(dense_layer):
        model.add(Dense(layer_size))
        model.add(Activation("relu"))

    model.add(Dense(1))
    model.add(Activation('sigmoid'))

    model.compile(optimizer='adam', loss="binary_crossentropy", metrics=['accuracy'])

    model.fit(x, y, batch_size=50, epochs=10, validation_split=0.3, callbacks=[tensorboard])

#TensorBoard optimize
dense_layers = [1,2,3]
layer_sizes = [32,64,128]
conv_layers = [1,3,6]

for dense_layer in dense_layers:
    for layer_size in layer_sizes:
        for conv_layer in conv_layers:
            NAME = "conv{}-nodes{}-dense{}-{}".format(conv_layer,layer_size,dense_layer,int(time.time()))
            modelBuilder(dense_layer,layer_size,conv_layer,NAME)

#put model to test

# def prepare(filepath):
#     IMG_SIZE = 100
#     img_array = cv2.imread(filepath,cv2.IMREAD_GRAYSCALE)
#     new_array = cv2.resize(img_array,(IMG_SIZE,IMG_SIZE))
#     return new_array.reshape(-1,IMG_SIZE,IMG_SIZE,1)
#
# prediction = model.predict([prepare('corg.jpg')])
# print(categories[int(prediction[0][0])])