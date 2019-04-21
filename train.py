
import logging
import os
import utils

from model.net.data_loader import DataLoader
from model.net import seq2class

##### SET HYPERPARAMETRS ###############
BATCH_SIZE = 32
DATA_PATH = os.path.join(os.getcwd(), '/Dataset/')
LEARNING_RATE = 1e04
EPOCHS = 3  # How many times you want to train the datasets

##########################################


def main():

    # Set the log file for debuging use
    utils.set_logger(os.path.join(os.getcwd(), 'train.log'))

    logging.info('Loading datasets...')

    data_loader = DataLoader(DATA_PATH)

    X_train, Y_train, X_val, Y_val = data_loader.get_train_data()
    X_test, Y_test = data_loader.get_test_data()

    logging.info('Building the model...')
    my_model = seq2class() # NEED TO PASS PARAMETERS SHIT

    print("Here is our model: ")
    logging.info(my_model.model.summary())

    logging.info('Training....')
    history = my_model.model.fit(X_train, Y_train, epochs=EPOCHS, verbose=1, batch_size=BATCH_SIZE, validation_data=(X_val, Y_val))

    # Plotting the loss history #
    plot = utils.Plotting(history)
    plot.plot_loss()
    plot.plot_accuracy()

    print('Testing...')
    loss, accuracy  = my_model.model.evaluate(X_test, Y_test)
    print('Testing loss', loss)
    print("Test accuracy", accuracy)

if __name__ == "__main__":
    main()


