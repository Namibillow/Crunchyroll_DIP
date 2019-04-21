from dan import *
from nami import *
from tony import *

import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--name", required=True,
                        help="name of the person you are recording")

    args = vars(parser.parse_args())
    name = args['name']
    if name == 'dan':
        storage = './Dataset/PD/'
    elif name == 'nami':
        storage = './Dataset/PN/'
    elif name == 'tony':
        storage = './Dataset/PT/'
    # Ask the person what they want to do/test
    step = input('What would you like to do: 1 to create a video, 2 to create data set(only if folders+files already chosen/made)\n')
    if step == '1':
        RecordVideo(args['name'], storage)
    ####### Only uncomment this if checking if it works##########
    # All of the files for each subject should be inside Frames/Base/
    elif step == '2':
        newDir = storage + 'Frames/'
        createNums(newDir)


    else:
        print(step + ' is not currently accepted, please run again')
    # openCam()
