'''define the model'''

from keras.layers import Input, Dense
from keras.models import Sequential
from keras import backend as K
from keras.layers import LSTM, Bidirectional, TimeDistributed
import os

class seq2class(depth=2):
    def __init__(self): # NEED TO PASS MORE PARAMS #
        self.model = self.build_model()

    def build_model(self):
        model = Sequential()
        model.add(Dense(32, activation='relu', input_shape=(SIZE * SIZE,)))

        # Add more ####################################################
        model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

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
