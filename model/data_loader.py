'''Load the data from Dataset'''

import os


class DataLoader():
    def __init__(self, data_path):
        '''
        data_path: path where datasets are stored
        '''
        self.data_path = data_path
        self._load_data()

    # Private function
    def _load_data():
        '''
        Load the images
        NEED TO NORMALIZE THE IMAGE
        RESCALE
        split videos to frames

        '''

    def get_train_data(self, validation_ratio=0.2, shuffle=False):
        '''
        split train and validation set
        return train and labels
        '''
        self.train_path = os.path.join(self.data_path, 'train')

        return X_train, Y_train, X_val, Y_val



    def get_test_data(self):
        '''
        return test and its labels should be tensor datatype

        '''
        self.test_path = os.path.join(self.data_path, 'train')

        return X_test, Y_test


