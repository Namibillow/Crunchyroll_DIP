'''Load the data from Dataset'''

import os


class DataLoader():
    def __init__(self, data_path):
        '''
        data_path: path where datasets are stored
        '''
        self.data_path = data_path
        self._load_data()
        self.label_index = {'dot':0, 'dash':1}
        self.index_label = {0: 'dot', 1: 'dash'}

    # Private function
    def _load_data(self):
        '''
        Load the images
        NEED TO NORMALIZE THE IMAGE
        split videos to frames
        '''
        all_imgs = []
        train_path = os.path.join(self.data_path, 'train')
        sub_folders = [i for i in os.listdir(train_path) if isdir(train_path, i)]
        for folder in sub_folders:
            imgs = [img for img in listdir(folder) if img.endswith('jpg')]






        # self.test_path = os.path.join(self.data_path, 'test')

        self.X_train = X_train.reshape([-1, SIZE, SIZE, CHANNEL])
        self.Y_train = pass
        self.X_val = pass
        self.Y_val = pass
        # self.X_test = pass
        # self.Y_test = pass

    def get_train_data(self, validation_ratio=0.2, shuffle=False):
        '''
        split train and validation set
        return train and labels
        '''
        return self.X_train, self.Y_train, self.X_val, self.Y_val



    def get_test_data(self):
        '''
        return test and its labels should be tensor datatype

        '''
        return self.X_test, self.Y_test


