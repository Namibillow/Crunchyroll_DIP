'''Load the data from Dataset'''

import os
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img

class DataLoader():
    def __init__(self, data_path):
        '''
        data_path: path where datasets are stored
        '''
        self.data_path = data_path
        self._load_data()
        self.label_index = {'dot':0, 'dash':1}
        self.index_label = {0: 'dot', 1: 'dash'}
        self.WIDTH = 636
        self.HEIGHT = 140
        self.CHANNEL = 3
        self.FRAMES = 7

    # Private function
    def _load_data(self):
        '''
        Load the images
        NEED TO NORMALIZE THE IMAGE
        Return
            X_train, Y_train : 5D numpy array [N samples, Time (frames), heigh, width, channel]
            Y_train : size N vector where its 0 or 1
        '''


        train_dataset = np.ndarray(shape=(self.FRAMES, self.HEIGHT, self.WIDTH,self.CHANNEL),dtype=np.float32)

        train_path = os.path.join(self.data_path, 'train')
        sub_folders = [i for i in os.listdir(train_path) if isdir(train_path, i)]
        for folder in sub_folders:
            imgs = [img for img in listdir(folder) if img.endswith('jpg')]
            for ind, img in enumerate(imgs):

                # TASK: read image
                x = img_to_array(img)

                # TASK: PERFORM Normalization each image divide by 255

                # TASK: also rescaling?? if so then need to change self.WIDTH, self.HEIGHT

                # Reshape image
                x = x.reshape((self.HEIGHT, self.WIDTH, 3))

                # assign it to index at
                train_dataset[ind] = x

            train_dataset = np.stack(train_dataset)


                # TASK: conver to numpy array at this point it will create 4D array [7, height, width, 3]




        # TASK Reshape following
        self.X_train = X_train.reshape([-1, self.FRAMES, self.HEIGHT, self.WIDTH, self.CHANNEL])
        self.Y_train = pass
        self.X_val = pass
        self.Y_val = pass
        self.X_test = pass
        self.Y_test = pass

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


