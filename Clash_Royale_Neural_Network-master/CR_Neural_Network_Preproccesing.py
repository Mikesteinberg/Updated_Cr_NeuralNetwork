#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 20:17:28 2018

@author: mike
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


from numpy.random import seed
seed(30)
from sklearn.utils import shuffle
# Importing the dataset
def Deck_Generator():
    with open("new_match_file_ladder.txt","r") as deck_file:
        while True:
            i = 0  
            while i < 2974000:
                for line in deck_file:
                    #Excludes the last three values and their commas.
                    line2 = line[-6:]
                    line = line[0: -7]
                    line_array = line.split(",")
                    line_array_two = line2.split(",")
                    deck_array = []
                    for num in line_array:
                        try:
                            deck_array.append(int(num))
                        except:
                            deck_array.append(float(num))
                    deck_array_tuple = tuple(deck_array)
                    winner_array = []
                    for num in line_array_two:
                        winner_array.append(int(num))
                    winner_array_tuple = tuple(winner_array)
                    i += 1
                    yield(deck_array_tuple, winner_array_tuple)
            deck_file.seek(0)
            continue
        deck_file.close()   

            
    

def Batch_Generator():
    my_deck = Deck_Generator()
    deck_batch_array = []
    win_batch_array = []
    while True:
        deck_batch_array = []
        win_batch_array = []
        for x in range (0,32):
            x = next(my_deck)
            deck_batch_array.append(x[0])
            win_batch_array.append(x[1])
        deck_batch_tuple = tuple(deck_batch_array)
        win_batch_tuple = tuple(win_batch_array)
        yield(np.array(deck_batch_tuple), np.array(win_batch_tuple))

my_batch = Batch_Generator()
    
#print(next(my_decks))

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout


classifier = Sequential()

#First Hidden Layer
classifier.add(Dense(kernel_initializer="uniform", units=80, activation="relu", input_dim = 188))
classifier.add(Dropout(p = 0.3))

classifier.add(Dense(kernel_initializer="uniform", units=30, activation="relu"))
classifier.add(Dropout(p = 0.3))

classifier.add(Dense(kernel_initializer="uniform", units=3, activation="softmax"))

classifier.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
# Making Predictions and Evaluating the Model
classifier.fit_generator(my_batch, steps_per_epoch = 92937, epochs = 25, use_multiprocessing=False, initial_epoch = 0)


tuples = (0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,1,1,0,0,0,1,0,0,1,1,0,0,1,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
First_Probability = classifier.predict(np.array([tuples]))
tuples2 = (0,0,1,1,0,0,0,1,0,0,1,1,0,0,1,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0);
Second_Probability = classifier.predict(np.array([tuples2]))
Second_Probability_Reversed = np.fliplr(Second_Probability)
total_probability = (First_Probability + Second_Probability_Reversed)/2

classifier.save("new_ladder_model.h5")

