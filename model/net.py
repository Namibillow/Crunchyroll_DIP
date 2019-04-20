'''define the model'''

from keras.layers import Input, Dense
from keras.models import Model
from keras import backend as K
from keras.layers import LSTM, Bidirectional, TimeDistributed


def s2c(depth=2):
    print('Building the model...')

    for dep in range(depth):
        pass
