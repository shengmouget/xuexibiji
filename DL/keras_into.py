# coding: utf-8 
# @Time    : 2022/11/6 下午8:01
import numpy as np
from tensorflow import keras
from tensorflow.keras.datasets import fashion_mnist
import os
import cv2
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, Dropout, MaxPool2D, Flatten, Dense
from tensorflow.keras.losses import categorical_crossentropy  # 十分类
from tensorflow.keras.optimizers import SGD, RMSprop, Adam
from tensorflow.keras.utils import to_categorical
import tensorflow as tf

if __name__ == '__main__':
    np.set_printoptions(edgeitems=5)
    (x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()
    # np.set_printoptions(linewidth=1000)
    type_names = ['T-shirt', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
    # # print(x_train[0])
    # M,_,_ = x_train.shape
    # output_path = 'fashion_minist'
    # for i in range(M):
    #     if i % 5000 == 0:
    #         print(f'{0}%({1}/{2})'.format(i/M,i,M))
    #     type_name = type_names[y_train[i]]
    #     image_path = os.path.join(output_path,type_name)
    #     if not os.path.exists(image_path):
    #         os.mkdir(image_path)
    #     cv2.imwrite(os.path.join(image_path,str(i+1)+'.png'), x_train[0])
    # 变成单通道
    x_train = x_train.reshape(-1, 28, 28, 1) / 255
    x_test = x_test.reshape(-1, 28, 28, 1) / 255
    y_train = to_categorical(y_train)
    y_test = to_categorical(y_test)
    model = Sequential()
    #     卷积层
    model.add(Conv2D(6, 3, padding='same', activation='relu', input_shape=(28, 28, 1)))
    model.add(MaxPool2D(2, 2, padding='valid'))
    model.add(Conv2D(16, 3, padding='same', activation='relu'))
    model.add(MaxPool2D(2, 2, padding='valid'))
    model.add(Conv2D(32, 3, padding='same', activation='relu'))
    model.add(MaxPool2D(2, 2, padding='valid'))
    model.add(Flatten())  # 展平
    # 全连接
    model.add(Dense(64, activation='relu'))
    model.add(Dense(10, activation='softmax'))
    model.summary()
    model.compile(optimizer=Adam(learning_rate=0.001), loss=categorical_crossentropy, metrics=['acc'])
    model.fit(x_test, y_train, epochs=10, batch_size=32, validation_split=0.1)
