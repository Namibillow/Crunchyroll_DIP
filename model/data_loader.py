'''Load the data from Dataset'''

import os
from keras.preprocessing.image import img_to_array, load_img
import numpy as np

from sklearn.model_selection import train_test_split

class DataLoader():
    def __init__(self, data_path):
        '''
        data_path: path where datasets are stored
        '''
        self.data_path = data_path
        self._load_data()
        self.label_index = {'dot':0, 'dash':1}
        self.index_label = {0: 'dot', 1: 'dash'}

        # Manually setting change as if we need to
        self.WIDTH = 636
        self.HEIGHT = 140
        self.CHANNEL = 3
        self.FRAMES = 7
        self.NUM_EXAMPLES = 588
    # Private function
    def _load_data(self):
        '''
        Load the images
        NEED TO NORMALIZE THE IMAGE
        Return
            X_train, X_val : 5D numpy array [N samples, Time (frames), heigh, width, channel]
            Y_train, Y_val : size N by 1 vector where it contains 0 or 1
            X_test, Y_test

        '''
        # Need fix but general idea 5d idk if this is efficient
        X_train = np.zeros((self.NUM_EXAMPLES, self.FRAMES, self.HEIGHT, self.WIDTH,self.CHANNEL))

        # 4d
        train_dataset = np.ndarray(shape=(self.FRAMES, self.HEIGHT, self.WIDTH,self.CHANNEL),dtype=np.float32)

        # labels
        Y_train = np.zeros(self.NUM_EXAMPLES)

        train_path = os.path.join(self.data_path, 'train')
        sub_folders = [i for i in os.listdir(train_path) if os.isdir(train_path, i)]

        for i, folder in enumerate(sub_folders):

            # get the label from the folder name eg "p1_dash" then this video is dash
            label = folder.split('_')[-1]
            Y_train[i] = self.label_index[label]

            imgs = [img for img in os.listdir(folder) if img.endswith('jpg')]
            for ind, img in enumerate(imgs):

                # TASK: read image
                img = load_img(img)

                # TASK: Convert to array
                x = img_to_array(img)

                # TASK: PERFORM Normalization each image divide by x./255

                # TASK: also rescaling?? if so then need to change self.WIDTH, self.HEIGHT

                # Reshape image to 3D
                x = x.reshape((self.HEIGHT, self.WIDTH, self.CHANNEL))

                # assign x to our 4D array
                train_dataset[ind] = x

            X_train[i] = train_dataset


        assert self.X_train.ndim == 5
        assert self.X_train.shape[0] == self.NUM_EXAMPLES


        Y_train = Y_train.reshape(Y_train.shape[0], -1)
        # Splits 20% to test set
        X_train, self.X_test, y_train, self.y_test = train_test_split(X_train, Y_train, test_size=0.2, random_state=1)

        # Split 20% to validation
        self.X_train, self.X_val, self.y_train, self.y_val = train_test_split(X_train, y_train, test_size=0.2, random_state=1)

    def get_train_data(self, validation_ratio=0.2, shuffle=False):
        '''
        split train and validation set
        return train and labels
        '''


        return self.X_train, self.y_train, self.X_val, self.y_val



    def get_test_data(self):
        '''
        return test and its labels should be tensor datatype

        '''
        return self.X_test, self.y_test


