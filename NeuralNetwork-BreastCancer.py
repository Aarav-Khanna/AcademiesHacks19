import numpy as np
from random import randint
import pandas as pd
#import pandas
from keras import optimizers
from keras.wrappers.scikit_learn import KerasRegressor
import csv
from keras.models import Sequential
from keras.models import load_model
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Convolution2D, MaxPooling2D
from keras.optimizers import RMSprop, Adam
from keras.utils import np_utils

#for testing data (no labels)
def getDataUnlabeled():
    x = []
    input = open("testingdata.csv").read().split("\n")
    for index, i in enumerate(input):
        inputArray = i.split(",")
        if(len(inputArray)==9): #number of features           
            x.append(inputArray)
        else:
            print(len(inputArray))
    return x

#for training data (with labels)
def getDataLabeled():
    x = []
    y = []
    input = open("trainingdata.csv").read().split("\n")
    for i in input:
        inputArray = i.split(",")
        if(len(inputArray)==10): #number of features + number of labels        
            exp = inputArray.pop(len(inputArray)-1)
            x.append(inputArray)
            y.append(exp)
        else:
            print(len(inputArray))
    return x,y
  
X_train, y_train = getDataLabeled()
X_test = getDataUnlabeled()

X = np.array(X_train)
y = np.array(y_train)
#X=X.split(" ")

X = X.reshape(174, 9)
y = y.reshape(174)

#X = X.astype('float32')
#y = y.astype('float32')

model = Sequential()
#model.add(Dense(128, kernel_initializer='normal', activation='relu'))
model.add(Dense(64, kernel_initializer='normal', activation='sigmoid'))
model.add(Dense(32, kernel_initializer='normal', activation='sigmoid'))
#model.add(Dense(16, kernel_initializer='normal', activation='sigmoid'))
model.add(Dense(1, kernel_initializer='normal', activation='sigmoid'))
# Compile model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(X, y, batch_size = 2, epochs = 35, verbose = 1)

x_test = np.array(X_test)
x_test = x_test.reshape(174, 9)
x_test = x_test.astype("float32")
y_test = model.predict(x_test)

#y_test = np.argmax(y_test, axis = 1)
#pass array of labels and method will generate output txt
def generateOutputFile(y_test):
    with open('out.txt', 'w') as f:
        f.write("id,class\n")
        for i in range(len(y_test)):
            if y_test[i] < 0.5:
                prediction = 0
            else:
                prediction = 1
            f.write(str(i+1)+","+str(prediction)+"\n")

generateOutputFile(y_test)
