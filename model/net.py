'''define the model'''

from keras.layers import Input, Dense,Flatten
from keras.models import Sequential
from keras import backend as K
from keras.layers import LSTM, Bidirectional, TimeDistributed
from keras.layers import Conv2D,MaxPooling2D, Dropout
import os

class seq2class(depth=2):
    def __init__(self): # NEED TO PASS MORE PARAMS #
        self.model = self.build_model()

    def build_model(self, width, height, frames):
        '''
        '''
        # Fix parameters ####
        # Need to decided on model architecture#
        # should we use pre-trained model??
        model = Sequential()
        # CNN part
        model.add(TimeDistributed(Conv2D(64,(5,5), activation='relu'), input_shape=(frames, width, height, 3)))

        model.add(TimeDistributed(MaxPooling2D((2, 2), strides=(1, 1))))

        model.add(TimeDistributed(Conv2D(128, (4,4), activation='relu')))
        model.add(TimeDistributed(MaxPooling2D((2, 2), strides=(2, 2))))

        model.add(TimeDistributed(Conv2D(256, (4,4), activation='relu')))
        model.add(TimeDistributed(MaxPooling2D((2, 2), strides=(2, 2))))

        # extract features and dropout
        model.add(TimeDistributed(Flatten()))
        model.add(Dropout(0.5))

        # NOW feed to RNN
        model.add(LSTM(256, return_sequences=False, dropout=0.5))
        # Only returns last output

    # classifier with sigmoid activation for multilabel
        model.add(Dense(1, activation='sigmoid'))
        # Add more ####################################################
        model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

        return model

    # save function that saves the checkpoint in the path defined in the config file
    def save_model(self, checkpoint_path=os.path.join(os.getcwd(), '/check_point')):
        if self.model is None:
            raise Exception("You have to build the model first.")

        print("Saving model...")
        self.model.save_weights(checkpoint_path)
        print("Model saved")


    # load latest checkpoint from the experiment path defined in the config file
    def load_model(self, checkpoint_path=None):
        if self.model is None:
            raise Exception("You have to build the model first.")

        try:
            print("Loading model checkpoint {} ...\n".format(checkpoint_path))
            self.model.load_weights(checkpoint_path)
            print("Model loaded")
        except ValueError:
            print('Not a valid check_point')
